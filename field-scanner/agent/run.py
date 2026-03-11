#!/usr/bin/env python3
"""
DN Field Scanner — Autonomous Research Agent
=============================================

Daily cycle:
  1. Fetch recent papers from Semantic Scholar across target domains
  2. Select 2 strain candidates + 1 validation candidate
  3. Interpret each through the DN Framework's dimensional architecture
  4. Score on strain/validation axes (0–10 each)
  5. Update state/model.md and tensions/open.md
  6. Output cycle file to cycles/YYYY-MM-DD.md
  7. Append scores to scoring/scores.jsonl
  8. Regenerate scoring/distribution.png

Requires:
  - ANTHROPIC_API_KEY environment variable
  - Python 3.10+
  - Dependencies: anthropic, requests, matplotlib
"""

import os
import sys
import json
import time
import random
import logging
import datetime
from pathlib import Path
from typing import Optional

import requests
import anthropic
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent  # field-scanner/
STATE_MODEL = REPO_ROOT / "state" / "model.md"
TENSIONS_OPEN = REPO_ROOT / "tensions" / "open.md"
CYCLES_DIR = REPO_ROOT / "cycles"
SCORES_FILE = REPO_ROOT / "scoring" / "scores.jsonl"
DISTRIBUTION_PNG = REPO_ROOT / "scoring" / "distribution.png"
TENSION_LEDGER = REPO_ROOT / "tensions" / "ledger.md"
PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
CHARTER_PATH = PROMPTS_DIR / "interpretation_charter.md"

TODAY = datetime.date.today().isoformat()

CLAUDE_MODEL = "claude-opus-4-6"
MAX_TOKENS = 16_000

# Semantic Scholar search domains — broad enough to stress-test domain universality
SEARCH_QUERIES = [
    "organizational intelligence decision making",
    "cognitive development dimensional progression",
    "complexity theory emergent systems",
    "network science information flow fidelity",
    "fuzzy systems multi-criteria decision making",
    "recursive learning iterative refinement",
    "consciousness studies self-awareness",
    "systems dynamics feedback loops",
    "creativity innovation emergence",
    "education scaffolding developmental stages",
    "group decision making uncertainty",
    "knowledge management organizational learning",
    "identity formation psychological development",
    "entropy information degradation temporal",
    "resonance synchronization coupled systems",
]

# Map Semantic Scholar fields-of-study to DN scanner domain labels
DOMAIN_MAP = {
    "Business": "business-strategy",
    "Economics": "business-strategy",
    "Psychology": "cognitive-psychology",
    "Sociology": "organizational-behavior",
    "Education": "education",
    "Computer Science": "complexity-theory",
    "Mathematics": "fuzzy-systems",
    "Physics": "complexity-theory",
    "Biology": "systems-dynamics",
    "Philosophy": "consciousness-studies",
    "Political Science": "decision-science",
    "Medicine": "systems-dynamics",
    "Engineering": "network-science",
    "Environmental Science": "systems-dynamics",
    "Art": "creativity-research",
    "Linguistics": "cognitive-psychology",
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("dn-field-scanner")

# ---------------------------------------------------------------------------
# Semantic Scholar API
# ---------------------------------------------------------------------------

S2_API = "https://api.semanticscholar.org/graph/v1"
S2_HEADERS = {}
_s2_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
if _s2_key:
    S2_HEADERS["x-api-key"] = _s2_key


def fetch_recent_papers(max_per_query: int = 15) -> list[dict]:
    """
    Fetch recent papers across all search domains.
    Returns a deduplicated list of paper dicts.
    """
    seen_ids: set[str] = set()
    papers: list[dict] = []

    # Calculate date window: papers from the last 14 days
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=14)
    date_range = f"{start_date.isoformat()}:{end_date.isoformat()}"

    for query in SEARCH_QUERIES:
        try:
            log.info(f"Searching: {query}")
            resp = requests.get(
                f"{S2_API}/paper/search",
                params={
                    "query": query,
                    "limit": max_per_query,
                    "fields": "title,abstract,authors,url,year,fieldsOfStudy,publicationDate,externalIds,citationCount",
                    "publicationDateOrYear": date_range,
                    "sort": "publicationDate:desc",
                },
                headers=S2_HEADERS,
                timeout=30,
            )

            if resp.status_code == 429:
                log.warning("Rate limited by Semantic Scholar. Waiting 60s...")
                time.sleep(60)
                continue

            if resp.status_code != 200:
                log.warning(f"S2 returned {resp.status_code} for query: {query}")
                continue

            data = resp.json()
            for paper in data.get("data", []):
                pid = paper.get("paperId")
                if pid and pid not in seen_ids and paper.get("abstract"):
                    seen_ids.add(pid)
                    papers.append(paper)

            # Respect rate limits
            time.sleep(1.5)

        except Exception as e:
            log.error(f"Error fetching papers for '{query}': {e}")
            continue

    log.info(f"Fetched {len(papers)} unique papers with abstracts")
    return papers


def classify_domain(paper: dict) -> str:
    """Map a paper's fields of study to a DN scanner domain label."""
    fields = paper.get("fieldsOfStudy") or []
    for field in fields:
        if field in DOMAIN_MAP:
            return DOMAIN_MAP[field]
    return "general"


# ---------------------------------------------------------------------------
# Paper Selection via Claude
# ---------------------------------------------------------------------------

def build_selection_prompt(papers: list[dict]) -> str:
    """Build the prompt that asks Claude to select 2 strain + 1 validation candidates."""
    paper_summaries = []
    for i, p in enumerate(papers):
        authors = ", ".join(a.get("name", "Unknown") for a in (p.get("authors") or [])[:3])
        if len(p.get("authors", [])) > 3:
            authors += " et al."
        domain = classify_domain(p)
        abstract = (p.get("abstract") or "")[:600]
        paper_summaries.append(
            f"[{i}] \"{p.get('title', 'Untitled')}\"\n"
            f"    Authors: {authors}\n"
            f"    Domain: {domain}\n"
            f"    Abstract: {abstract}\n"
        )

    papers_block = "\n".join(paper_summaries)

    return f"""You are the selection engine for the DN Field Scanner, an autonomous research system that stress-tests the DN Framework against external academic research.

Below are {len(papers)} recent papers. Select exactly 3:
- 2 STRAIN candidates: papers most likely to CHALLENGE the DN Framework. Prioritize:
  • Research that formalizes something DN handles informally (e.g., mathematical models exceeding DN's metric precision)
  • Findings suggesting intelligence does NOT follow a dimensional progression
  • Evidence of successful frameworks using fundamentally different structural primitives
  • Cross-disciplinary integration achieved without anything resembling pillars, dimensions, or fields
- 1 VALIDATION candidate: the paper most likely to INDEPENDENTLY CONFIRM DN's structural claims. Prioritize:
  • Research independently arriving at three-axis evaluation systems
  • Evidence of natural dimensional progression in learning, development, or growth
  • Findings about information fidelity loss in transmission (flow parallels)
  • Studies confirming recursive refinement outperforms linear accumulation

THE DN FRAMEWORK IN BRIEF (for selection context):
- 1D–9D dimensional progression: Spark → Reaction → Context → Temporal → Singularity → Connection → Manifestation → Recursion → Frontier
- Three pillar metrics: Heart (motivational force), Truth (structural integrity), Nuance (contextual sensitivity)
- Five forces: Gravity, Resonance, Transmutation, Entropy, Shadow
- Flow as transport principle (not a sixth force)
- Domain universality claim: the architecture does not change across domains

Respond ONLY with valid JSON (no markdown, no explanation):
{{
  "strain_1": {{ "index": <int>, "rationale": "<why this paper strains DN>" }},
  "strain_2": {{ "index": <int>, "rationale": "<why this paper strains DN>" }},
  "validation": {{ "index": <int>, "rationale": "<why this paper validates DN>" }}
}}

PAPERS:
{papers_block}"""


def select_papers(papers: list[dict], client: anthropic.Anthropic) -> list[dict]:
    """
    Use Claude to select 2 strain candidates and 1 validation candidate.
    Returns list of 3 paper dicts with selection metadata attached.
    """
    if len(papers) < 3:
        log.error(f"Only {len(papers)} papers fetched. Need at least 3. Using all.")
        for p in papers:
            p["_selection_role"] = "strain"
            p["_selection_rationale"] = "Insufficient papers; included by default."
        return papers

    # If we have a very large number, sample down to keep the prompt manageable
    if len(papers) > 60:
        papers_for_selection = random.sample(papers, 60)
    else:
        papers_for_selection = papers

    prompt = build_selection_prompt(papers_for_selection)

    log.info("Requesting paper selection from Claude...")
    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1000,
        temperature=0.3,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()
    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        if raw.endswith("```"):
            raw = raw.rsplit("```", 1)[0]
    raw = raw.strip()

    selection = json.loads(raw)

    selected = []
    for role_key, role_label in [("strain_1", "strain"), ("strain_2", "strain"), ("validation", "validation")]:
        idx = selection[role_key]["index"]
        paper = papers_for_selection[idx].copy()
        paper["_selection_role"] = role_label
        paper["_selection_rationale"] = selection[role_key]["rationale"]
        selected.append(paper)

    log.info(f"Selected papers: {[p.get('title', '')[:60] for p in selected]}")
    return selected


# ---------------------------------------------------------------------------
# Interpretation & Scoring via Claude
# ---------------------------------------------------------------------------

def load_dn_context() -> str:
    """Load the DN Kernel, Glossary, and Interpretation Charter for grounding context."""
    context_parts = []

    kernel_path = PROMPTS_DIR / "dn_kernel_excerpt.md"
    glossary_path = PROMPTS_DIR / "dn_glossary_excerpt.md"

    # Try prompt-directory excerpts first, fall back to repo-level copies
    for label, path, fallbacks in [
        ("DN KERNEL", kernel_path, [REPO_ROOT.parent / "DN_Kernel.md", REPO_ROOT.parent / "DN_Kernel_v18.md"]),
        ("DN GLOSSARY", glossary_path, [REPO_ROOT.parent / "DN_Glossary_of_Terms.md", REPO_ROOT.parent / "DN_Glossary_of_Terms_v15.md"]),
    ]:
        loaded = False
        for p in [path] + fallbacks:
            if p.exists():
                text = p.read_text(encoding="utf-8")
                # Truncate if very long to stay within context limits
                if len(text) > 40_000:
                    text = text[:40_000] + "\n\n[... truncated for context window ...]"
                context_parts.append(f"<{label.lower().replace(' ', '_')}>\n{text}\n</{label.lower().replace(' ', '_')}>")
                loaded = True
                break
        if not loaded:
            log.warning(f"Could not load {label}. Interpretation will proceed without it.")

    # Load the Interpretation Charter — this teaches the agent HOW to read the Kernel
    if CHARTER_PATH.exists():
        charter_text = CHARTER_PATH.read_text(encoding="utf-8")
        context_parts.append(f"<interpretation_charter>\n{charter_text}\n</interpretation_charter>")
        log.info("Loaded Interpretation Charter.")
    else:
        log.warning("Interpretation Charter not found. Agent will interpret without architectural guidance.")

    return "\n\n".join(context_parts)


def load_current_state() -> str:
    """Load current model state and open tensions for context."""
    parts = []
    if STATE_MODEL.exists():
        text = STATE_MODEL.read_text(encoding="utf-8")
        if len(text) > 8000:
            text = text[:8000] + "\n\n[... truncated ...]"
        parts.append(f"<current_model_state>\n{text}\n</current_model_state>")
    if TENSIONS_OPEN.exists():
        text = TENSIONS_OPEN.read_text(encoding="utf-8")
        if len(text) > 4000:
            text = text[:4000] + "\n\n[... truncated ...]"
        parts.append(f"<open_tensions>\n{text}\n</open_tensions>")
    return "\n\n".join(parts)


def build_interpretation_prompt(paper: dict, dn_context: str, current_state: str) -> str:
    """Build the full interpretation + scoring prompt for a single paper."""
    authors = ", ".join(a.get("name", "Unknown") for a in (paper.get("authors") or [])[:5])
    if len(paper.get("authors", [])) > 5:
        authors += " et al."

    domain = classify_domain(paper)
    role = paper.get("_selection_role", "unknown")
    selection_rationale = paper.get("_selection_rationale", "")
    abstract = paper.get("abstract", "No abstract available.")
    url = paper.get("url", "")

    # Build external IDs
    ext_ids = paper.get("externalIds") or {}
    doi = ext_ids.get("DOI", "")
    arxiv = ext_ids.get("ArXiv", "")
    source_url = url
    if doi:
        source_url = f"https://doi.org/{doi}"
    elif arxiv:
        source_url = f"https://arxiv.org/abs/{arxiv}"

    return f"""You are the interpretive engine for the DN Field Scanner. Your job is to honestly assess how this paper relates to the DN Framework's structural claims. Prioritize honesty about the framework's limits over smooth narrative. Comfortable coherence is failure. Productive tension is success.

CRITICAL: You have been provided an Interpretation Charter alongside the Kernel and Glossary. The Charter teaches you HOW to read the Kernel. Follow its guidance on:
- What "dimensional progression" actually means (structural mapping, NOT sequential climbing)
- Nested dimensionality and the depth defense against falsifiability claims
- The maturity weighting of Kernel sections (foundational vs. recent)
- The "describing DN back to itself" trap (narrative flexibility ≠ validation)
- What genuine strain looks like vs. vocabulary differences
- Force model interpretation (dynamics vs. mechanisms)
- The entropy event horizon open question

{dn_context}

{current_state}

PAPER TO INTERPRET:
Title: {paper.get('title', 'Untitled')}
Authors: {authors}
Domain: {domain}
Selection role: {role} (rationale: {selection_rationale})
URL: {source_url}
Abstract: {abstract}

INTERPRETATION PRINCIPLES:
1. DN is descriptive, not prescriptive. The 1D-9D architecture is a MAP OF STRUCTURE, not a sequential climbing mandate. Ask "does this system resist MAPPING?" not "does this system fail to PROGRESS?"
2. Domain universality is the big claim. Does this paper's domain exhibit dimensional structure when mapped, or does the mapping produce contradictions?
3. Pillar independence matters. Papers showing evaluation systems collapsing into fewer axes (or requiring more) are structurally significant.
4. Mathematical rigor outranks narrative elegance. If this paper formalizes something DN handles only narratively, that's productive tension — note it as "formal exceeding."
5. Shadow is load-bearing. Papers engaging with absence, hesitancy, uncertainty, negative space test Section 4 of the Kernel. Papers treating absence as mere deficiency (to fix) create tension; papers treating absence as structurally generative (shaping the system) align.
6. Recursion is the mechanism. Papers showing recursive approaches outperform linear ones validate Axiom 3. Papers showing linear approaches working fine strain it.
7. Forces describe DYNAMICS, not mechanisms. A paper showing coherence through a novel mechanism is not contradicting Resonance unless the structural DYNAMIC (lateral binding between peer intelligence) is absent. Ask: "Is the dynamic absent, or just the expected mechanism?"
8. Maturity matters. Strain against foundational claims (dimensional architecture, pillar independence, domain universality) is categorically more significant than strain against recent formalizations (five-force naming, transport properties, thermodynamic regime note). Note which you are testing.

SCORING RULES:
- Strain (0–10): How much this paper resists DN interpretation. Scores above 5 require identification of a specific DN claim (Kernel section, axiom, or invariant) that is challenged.
- Validation (0–10): How specifically this paper validates DN — not just consistency but structural specificity. Scores above 3 require articulable structural specificity: name WHICH axiom, invariant, or architectural claim the paper independently confirms. "Compatible with DN" is not validation. Before scoring above 3, ask: "If DN did not exist, would I still recognize this paper as arriving at the same structural principle?"

Respond ONLY with valid JSON (no markdown fences, no explanation outside the JSON):
{{
  "interpretation": "<Your full interpretive analysis. 3-5 paragraphs. Be specific about dimensional mapping, pillar engagement, force dynamics. Identify exactly where the framework handles this paper well and where it strains or fails. Follow the Charter's guidance throughout.>",
  "strain": <integer 0-10>,
  "validation": <integer 0-10>,
  "strain_rationale": "<What specific DN claim is challenged and how. If strain <= 5, what general tension exists. If strain > 5, name the Kernel section/axiom.>",
  "validation_rationale": "<What specific DN structural principle is independently confirmed. If validation <= 3, note that compatibility alone is not validation. If validation > 3, name the axiom/invariant.>",
  "maturity_target": "<Which maturity tier does this paper's strain/validation primarily engage? One of: 'foundational', 'mature', 'recent'. See Charter §4.>",
  "dn_sections_engaged": ["<list of Kernel sections, e.g., '§0.3 Axiom 3', '§3 Pillar Metric', '§4.1 Shadow Dimension Map'>"],
  "dimensions_engaged": ["<list of dimensions engaged, e.g., '2D', '5D', '8D'>"],
  "pillars_engaged": ["<subset of: 'Heart', 'Truth', 'Nuance'>"],
  "forces_engaged": ["<subset of: 'Gravity', 'Resonance', 'Transmutation', 'Entropy', 'Shadow', 'Flow'>"],
  "tension_generated": "<Description of a new tension to add to the tension ledger, or null if none. Include a short tension_id slug for tracking, e.g., 'entropy-impossibility-conditions'>",
  "model_update": "<Brief description of any update warranted to state/model.md, or null if none>"
}}"""


def interpret_paper(paper: dict, dn_context: str, current_state: str, client: anthropic.Anthropic) -> dict:
    """Interpret a single paper through the DN Framework and return scored result."""
    prompt = build_interpretation_prompt(paper, dn_context, current_state)

    log.info(f"Interpreting: {paper.get('title', '')[:80]}...")
    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=MAX_TOKENS,
        temperature=0.4,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()
    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        if raw.endswith("```"):
            raw = raw.rsplit("```", 1)[0]
    raw = raw.strip()

    result = json.loads(raw)

    # Attach paper metadata
    authors = [a.get("name", "Unknown") for a in (paper.get("authors") or [])[:5]]
    ext_ids = paper.get("externalIds") or {}
    doi = ext_ids.get("DOI", "")
    arxiv = ext_ids.get("ArXiv", "")
    source_url = paper.get("url", "")
    if doi:
        source_url = f"https://doi.org/{doi}"
    elif arxiv:
        source_url = f"https://arxiv.org/abs/{arxiv}"

    result["date"] = TODAY
    result["paper"] = {
        "title": paper.get("title", "Untitled"),
        "authors": authors,
        "source": "semantic-scholar",
        "url": source_url,
        "domain": classify_domain(paper),
    }
    result["selection_role"] = paper.get("_selection_role", "unknown")
    result["selection_rationale"] = paper.get("_selection_rationale", "")

    return result


# ---------------------------------------------------------------------------
# State Updates
# ---------------------------------------------------------------------------

def update_model_state(results: list[dict]) -> None:
    """Append a dated update section to state/model.md if any result warrants it."""
    updates = [r for r in results if r.get("model_update")]
    if not updates:
        log.info("No model updates warranted this cycle.")
        return

    STATE_MODEL.parent.mkdir(parents=True, exist_ok=True)

    section = f"\n\n---\n\n### Cycle Update — {TODAY}\n\n"
    for r in updates:
        title = r["paper"]["title"]
        role = r.get("selection_role", "unknown")
        strain = r.get("strain", 0)
        validation = r.get("validation", 0)
        update_text = r["model_update"]
        section += (
            f"**{title}** ({role}, strain: {strain}, validation: {validation})\n\n"
            f"{update_text}\n\n"
        )

    with open(STATE_MODEL, "a", encoding="utf-8") as f:
        f.write(section)

    log.info(f"Updated state/model.md with {len(updates)} entries.")


def update_tensions(results: list[dict]) -> None:
    """Update both tensions/open.md (raw log) and tensions/ledger.md (structured tracking)."""
    tensions = [r for r in results if r.get("tension_generated")]
    if not tensions:
        log.info("No new tensions generated this cycle.")
        return

    TENSIONS_OPEN.parent.mkdir(parents=True, exist_ok=True)

    # --- Append raw tensions to open.md (unchanged behavior) ---
    section = f"\n\n---\n\n### New Tensions — {TODAY}\n\n"
    for r in tensions:
        title = r["paper"]["title"]
        strain = r.get("strain", 0)
        tension_text = r["tension_generated"]
        sections_engaged = ", ".join(r.get("dn_sections_engaged", []))
        section += (
            f"**Source:** {title} (strain: {strain})\n"
            f"**Kernel sections engaged:** {sections_engaged}\n"
            f"**Tension:** {tension_text}\n\n"
        )

    with open(TENSIONS_OPEN, "a", encoding="utf-8") as f:
        f.write(section)

    log.info(f"Added {len(tensions)} new tensions to tensions/open.md.")

    # --- Update structured Tension Ledger ---
    _update_tension_ledger(tensions)


def _update_tension_ledger(new_tensions: list[dict]) -> None:
    """
    Maintain a structured tension ledger that consolidates related tensions,
    tracks citation counts, and promotes tensions that cross the review threshold.

    The ledger is a markdown file with a parseable structure:
    - Each tension has an ID, description, citation count, source papers, maturity target, and status
    - Status: 'tracking' (< 3 citations), 'review' (>= 3 citations), 'resolved', 'malformed'
    - The REVIEW QUEUE section lists tensions ready for human attention
    """
    REVIEW_THRESHOLD = 3

    # Load existing ledger or create new one
    if TENSION_LEDGER.exists():
        ledger_text = TENSION_LEDGER.read_text(encoding="utf-8")
    else:
        ledger_text = ""

    # Parse existing tensions from ledger (simple structured format)
    # Format: ### TENSION_ID | status | citations: N
    import re
    existing_tensions: dict[str, dict] = {}
    tension_blocks = re.split(r'(?=^### [a-z])', ledger_text, flags=re.MULTILINE)
    for block in tension_blocks:
        header_match = re.match(
            r'^### ([a-z0-9_-]+) \| status: (\w+) \| citations: (\d+)',
            block.strip()
        )
        if header_match:
            tid = header_match.group(1)
            existing_tensions[tid] = {
                "id": tid,
                "status": header_match.group(2),
                "citations": int(header_match.group(3)),
                "block": block.strip(),
            }

    # Process new tensions
    updated_ids = set()
    new_entries = []

    for r in new_tensions:
        tension_text = r.get("tension_generated", "")
        title = r.get("paper", {}).get("title", "Unknown")
        strain = r.get("strain", 0)
        maturity = r.get("maturity_target", "unknown")
        sections = ", ".join(r.get("dn_sections_engaged", []))

        # Extract tension_id if the agent included one (format: "tension_id: some-slug-here")
        tid_match = re.search(r'([a-z][a-z0-9_-]{2,40})', tension_text.lower().replace(" ", "-")[:60])
        tension_id = tid_match.group(1) if tid_match else f"tension-{TODAY}-{len(new_entries)}"

        # Check if this tension matches an existing one (by ID prefix match)
        matched_existing = None
        for eid, edata in existing_tensions.items():
            # Simple keyword overlap check — tensions with similar IDs are related
            if (eid in tension_id or tension_id in eid or
                    _tension_similarity(eid, tension_id) > 0.5):
                matched_existing = eid
                break

        if matched_existing:
            # Increment citation count on existing tension
            old = existing_tensions[matched_existing]
            new_count = old["citations"] + 1
            new_status = "review" if new_count >= REVIEW_THRESHOLD else old["status"]
            # Append new source to existing block
            updated_block = old["block"].replace(
                f"citations: {old['citations']}",
                f"citations: {new_count}"
            )
            if new_status != old["status"]:
                updated_block = updated_block.replace(
                    f"status: {old['status']}",
                    f"status: {new_status}"
                )
            updated_block += f"\n- [{TODAY}] {title} (strain: {strain})"
            existing_tensions[matched_existing]["block"] = updated_block
            existing_tensions[matched_existing]["citations"] = new_count
            existing_tensions[matched_existing]["status"] = new_status
            updated_ids.add(matched_existing)
            log.info(f"  Tension '{matched_existing}' now at {new_count} citations (status: {new_status})")
        else:
            # Create new tension entry
            entry = (
                f"### {tension_id} | status: tracking | citations: 1\n\n"
                f"**Maturity target:** {maturity}\n"
                f"**Kernel sections:** {sections}\n"
                f"**Description:** {tension_text}\n\n"
                f"**Sources:**\n"
                f"- [{TODAY}] {title} (strain: {strain})"
            )
            new_entries.append(entry)
            log.info(f"  New tension registered: '{tension_id}'")

    # Rebuild ledger
    header = (
        "# DN Field Scanner — Tension Ledger\n\n"
        "*Structured tracking of tensions across cycles. Tensions are promoted to*\n"
        "*the Review Queue when they accumulate 3+ independent citations.*\n\n"
        f"*Last updated: {TODAY}*\n\n"
    )

    # Collect review-ready tensions
    review_queue = []
    tracking = []
    resolved = []

    for tid, tdata in existing_tensions.items():
        if tdata["status"] == "review":
            review_queue.append(tdata["block"])
        elif tdata["status"] in ("resolved", "malformed"):
            resolved.append(tdata["block"])
        else:
            tracking.append(tdata["block"])

    # Add new entries to tracking
    tracking.extend(new_entries)

    sections = [header]

    if review_queue:
        sections.append("---\n\n## REVIEW QUEUE\n\n"
                       "*These tensions have been independently surfaced by 3+ papers.*\n"
                       "*They warrant human review for potential Kernel revision.*\n\n")
        sections.append("\n\n".join(review_queue))

    sections.append("\n\n---\n\n## TRACKING\n\n"
                   "*Active tensions accumulating citations.*\n\n")
    sections.append("\n\n".join(tracking) if tracking else "*No tensions currently tracking.*")

    if resolved:
        sections.append("\n\n---\n\n## RESOLVED / MALFORMED\n\n")
        sections.append("\n\n".join(resolved))

    TENSION_LEDGER.write_text("\n".join(sections), encoding="utf-8")
    log.info(f"Updated tension ledger: {len(review_queue)} in review, {len(tracking)} tracking.")


def _tension_similarity(a: str, b: str) -> float:
    """Simple word-overlap similarity between two tension IDs."""
    words_a = set(a.replace("-", " ").replace("_", " ").split())
    words_b = set(b.replace("-", " ").replace("_", " ").split())
    if not words_a or not words_b:
        return 0.0
    overlap = words_a & words_b
    return len(overlap) / min(len(words_a), len(words_b))


# ---------------------------------------------------------------------------
# Cycle File Output
# ---------------------------------------------------------------------------

def write_cycle_file(results: list[dict]) -> Path:
    """Write the per-cycle markdown file to cycles/YYYY-MM-DD.md."""
    CYCLES_DIR.mkdir(parents=True, exist_ok=True)
    cycle_path = CYCLES_DIR / f"{TODAY}.md"

    lines = [
        f"# DN Field Scanner — Cycle {TODAY}\n",
        f"\n**Papers processed:** {len(results)}\n",
        f"**Strain candidates:** {sum(1 for r in results if r.get('selection_role') == 'strain')}",
        f"**Validation candidates:** {sum(1 for r in results if r.get('selection_role') == 'validation')}",
        "",
    ]

    # Summary statistics
    avg_strain = sum(r.get("strain", 0) for r in results) / max(len(results), 1)
    avg_validation = sum(r.get("validation", 0) for r in results) / max(len(results), 1)
    lines.append(f"**Average strain:** {avg_strain:.1f} | **Average validation:** {avg_validation:.1f}\n")

    lines.append("---\n")

    for i, r in enumerate(results, 1):
        p = r.get("paper", {})
        lines.append(f"## Paper {i}: {p.get('title', 'Untitled')}\n")
        lines.append(f"**Authors:** {', '.join(p.get('authors', []))}")
        lines.append(f"**Domain:** {p.get('domain', 'unknown')}")
        lines.append(f"**URL:** {p.get('url', 'N/A')}")
        lines.append(f"**Selection role:** {r.get('selection_role', 'unknown')}")
        lines.append(f"**Selection rationale:** {r.get('selection_rationale', '')}\n")

        lines.append(f"### Scores\n")
        lines.append(f"| Metric | Score |")
        lines.append(f"|--------|-------|")
        lines.append(f"| Strain | {r.get('strain', 'N/A')} / 10 |")
        lines.append(f"| Validation | {r.get('validation', 'N/A')} / 10 |\n")

        lines.append(f"**Strain rationale:** {r.get('strain_rationale', 'N/A')}\n")
        lines.append(f"**Validation rationale:** {r.get('validation_rationale', 'N/A')}\n")

        lines.append(f"### DN Engagement\n")
        lines.append(f"- **Sections:** {', '.join(r.get('dn_sections_engaged', []))}")
        lines.append(f"- **Dimensions:** {', '.join(r.get('dimensions_engaged', []))}")
        lines.append(f"- **Pillars:** {', '.join(r.get('pillars_engaged', []))}")
        lines.append(f"- **Forces:** {', '.join(r.get('forces_engaged', []))}\n")

        lines.append(f"### Interpretation\n")
        lines.append(r.get("interpretation", "No interpretation produced."))
        lines.append("")

        if r.get("tension_generated"):
            lines.append(f"### Tension Generated\n")
            lines.append(r["tension_generated"])
            lines.append("")

        if r.get("model_update"):
            lines.append(f"### Model Update\n")
            lines.append(r["model_update"])
            lines.append("")

        lines.append("---\n")

    # Self-assessment section
    lines.append("## Cycle Self-Assessment\n")
    lines.append(f"This cycle processed {len(results)} papers across domains: "
                 f"{', '.join(set(r.get('paper', {}).get('domain', 'unknown') for r in results))}.\n")

    high_strain = [r for r in results if r.get("strain", 0) >= 5]
    high_val = [r for r in results if r.get("validation", 0) >= 5]
    if high_strain:
        lines.append(f"**High-strain findings ({len(high_strain)}):** These papers produced genuine structural "
                     f"tension with the DN Framework and may warrant Kernel-level attention.\n")
    if high_val:
        lines.append(f"**Strong validation findings ({len(high_val)}):** These papers independently confirmed "
                     f"specific DN structural claims with articulable specificity.\n")
    if not high_strain and not high_val:
        lines.append("**Assessment:** This cycle produced moderate findings without extreme strain or validation. "
                     "The framework handled these papers within its existing architecture.\n")

    cycle_path.write_text("\n".join(lines), encoding="utf-8")
    log.info(f"Wrote cycle file: {cycle_path}")
    return cycle_path


# ---------------------------------------------------------------------------
# Scoring Persistence & Visualization
# ---------------------------------------------------------------------------

def append_scores(results: list[dict]) -> None:
    """Append one JSON line per paper to scores.jsonl."""
    SCORES_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(SCORES_FILE, "a", encoding="utf-8") as f:
        for r in results:
            score_entry = {
                "date": r.get("date", TODAY),
                "paper": r.get("paper", {}),
                "strain": r.get("strain", 0),
                "validation": r.get("validation", 0),
                "strain_rationale": r.get("strain_rationale", ""),
                "validation_rationale": r.get("validation_rationale", ""),
                "dn_sections_engaged": r.get("dn_sections_engaged", []),
                "dimensions_engaged": r.get("dimensions_engaged", []),
                "pillars_engaged": r.get("pillars_engaged", []),
                "forces_engaged": r.get("forces_engaged", []),
                "tension_generated": r.get("tension_generated"),
                "model_update": r.get("model_update"),
            }
            f.write(json.dumps(score_entry) + "\n")

    log.info(f"Appended {len(results)} scores to {SCORES_FILE}")


def regenerate_distribution_plot() -> None:
    """Regenerate the scatter plot from scores.jsonl."""
    if not SCORES_FILE.exists():
        log.warning("No scores file found. Skipping plot generation.")
        return

    scores = []
    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    scores.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

    if not scores:
        log.warning("No scores to plot.")
        return

    strains = [s.get("strain", 0) for s in scores]
    validations = [s.get("validation", 0) for s in scores]
    domains = [s.get("paper", {}).get("domain", "unknown") for s in scores]

    # Color map by domain
    unique_domains = sorted(set(domains))
    cmap = plt.cm.get_cmap("tab20", max(len(unique_domains), 1))
    domain_colors = {d: cmap(i) for i, d in enumerate(unique_domains)}
    colors = [domain_colors[d] for d in domains]

    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    ax.scatter(strains, validations, c=colors, s=60, alpha=0.7, edgecolors="white", linewidth=0.5)

    # Quadrant lines
    ax.axhline(y=5, color="gray", linestyle="--", alpha=0.4)
    ax.axvline(x=5, color="gray", linestyle="--", alpha=0.4)

    # Quadrant labels
    ax.text(7.5, 7.5, "Productive\nfriction", ha="center", va="center", fontsize=9, alpha=0.5, style="italic")
    ax.text(2.5, 7.5, "Genuine\nconfirmation", ha="center", va="center", fontsize=9, alpha=0.5, style="italic")
    ax.text(7.5, 2.5, "Hard\nresistance", ha="center", va="center", fontsize=9, alpha=0.5, style="italic")
    ax.text(2.5, 2.5, "Neutral\nterritory", ha="center", va="center", fontsize=9, alpha=0.5, style="italic")

    ax.set_xlabel("Strain →", fontsize=11)
    ax.set_ylabel("Validation →", fontsize=11)
    ax.set_title(f"DN Field Scanner — Score Distribution ({len(scores)} papers)", fontsize=13)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 10.5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.15)

    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor=domain_colors[d],
               markersize=8, label=d)
        for d in unique_domains[:12]  # cap legend entries
    ]
    if legend_elements:
        ax.legend(handles=legend_elements, loc="upper left", fontsize=7, framealpha=0.7)

    fig.tight_layout()
    fig.savefig(DISTRIBUTION_PNG, dpi=150)
    plt.close(fig)
    log.info(f"Regenerated distribution plot: {DISTRIBUTION_PNG}")


# ---------------------------------------------------------------------------
# Main Cycle
# ---------------------------------------------------------------------------

def run_cycle() -> None:
    """Execute one complete DN Field Scanner cycle."""
    log.info(f"=== DN Field Scanner — Cycle {TODAY} ===")

    # Validate API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        log.error("ANTHROPIC_API_KEY not set. Aborting.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Step 1: Fetch papers
    log.info("Step 1: Fetching recent papers from Semantic Scholar...")
    papers = fetch_recent_papers()

    if not papers:
        log.error("No papers fetched. Aborting cycle.")
        sys.exit(1)

    # Step 2: Select papers
    log.info("Step 2: Selecting strain and validation candidates...")
    selected = select_papers(papers, client)

    # Step 3: Load DN context
    log.info("Step 3: Loading DN Framework context...")
    dn_context = load_dn_context()
    current_state = load_current_state()

    # Step 4: Interpret each paper
    log.info("Step 4: Interpreting selected papers...")
    results = []
    for paper in selected:
        try:
            result = interpret_paper(paper, dn_context, current_state, client)
            results.append(result)
            log.info(
                f"  → {paper.get('title', '')[:60]}: "
                f"strain={result.get('strain', '?')}, validation={result.get('validation', '?')}"
            )
        except Exception as e:
            log.error(f"Failed to interpret paper '{paper.get('title', '')}': {e}")
            continue

    if not results:
        log.error("No papers successfully interpreted. Aborting.")
        sys.exit(1)

    # Step 5: Update state
    log.info("Step 5: Updating state files...")
    update_model_state(results)
    update_tensions(results)

    # Step 6: Write cycle file
    log.info("Step 6: Writing cycle file...")
    cycle_path = write_cycle_file(results)

    # Step 7: Append scores
    log.info("Step 7: Appending scores...")
    append_scores(results)

    # Step 8: Regenerate visualization
    log.info("Step 8: Regenerating distribution plot...")
    regenerate_distribution_plot()

    # Summary
    avg_strain = sum(r.get("strain", 0) for r in results) / len(results)
    avg_validation = sum(r.get("validation", 0) for r in results) / len(results)
    log.info(f"=== Cycle complete ===")
    log.info(f"Papers interpreted: {len(results)}")
    log.info(f"Average strain: {avg_strain:.1f}, Average validation: {avg_validation:.1f}")
    log.info(f"Cycle file: {cycle_path}")


if __name__ == "__main__":
    run_cycle()
