# DN Field Scanner

An autonomous research system that interprets new academic findings through the DN Framework's dimensional architecture for intelligence.

## What This Is

DN Field Scanner is a self-running system. Every day, it:

1. Fetches recent papers from across disciplines — business strategy, cognitive science, organizational psychology, education, complexity theory, network science, fuzzy systems, decision science, and adjacent fields
2. Selects papers — 2 most likely to *strain* the framework, 1 most likely to offer genuine *validation*
3. Interprets those papers through the DN Framework's dimensional architecture, which holds that intelligence structures itself naturally through a 1D–9D progression governed by three pillar metrics (Heart, Truth, Nuance), five forces (Gravity, Resonance, Transmutation, Entropy, Shadow), and thermodynamic flow constraints
4. Updates its living model of the framework's cross-disciplinary standing based on what it finds
5. Tracks unresolved tensions — places where the framework fails, strains, or produces surprising structural descriptions

The system commits its outputs to this repository. **The git history is the Field Ledger** — each commit is a resolution event, an irreversible state update to the framework's developmental record.

## What To Read

- **[state/model.md](state/model.md)** — The system's current model of the DN Framework's cross-disciplinary standing. This is a living document that evolves with each cycle. The original seed content stays intact; updates are appended as dated sections.
- **[tensions/open.md](tensions/open.md)** — Unresolved states. Things the framework cannot yet account for, or places where external research formalizes something DN claims but with greater rigor. New tensions are added when cycles generate them. Tensions are only removed when they resolve into the state layer or are demonstrated to be malformed questions.
- **[cycles/](cycles/)** — One file per cycle. Each contains the full interpretive output: which papers were processed, where the framework strained, what changed, and the system's self-assessment.

## What This Is Not

This system is not trying to prove the DN Framework correct. It is stress-testing the framework against real research across domains. Comfortable coherence is failure. Productive tension is success. The interesting outputs are the places where the framework breaks or bends in unexpected ways — and especially where independent research arrives at structural principles DN already claims, since that's where domain universality either holds or doesn't.

## The DN Framework in Brief

The DN Framework is a domain-universal architecture for how intelligence organizes itself. Its formal specification layer, the **DN Kernel**, defines structural invariants that any system must respect to be DN-compliant. The core claims this system is testing:

- **Dimensional Progression (1D–9D):** Intelligence follows a natural progression from Spark (1D) through Reaction (2D), Context (3D), Temporal (4D), Singularity (5D), Connection (6D), Manifestation (7D), Recursion (8D), to Frontier (9D). This progression is descriptive, not prescriptive.
- **Pillar Metric:** Heart (motivational force), Truth (structural integrity), and Nuance (contextual sensitivity) are universal governing metrics for intelligence in any domain.
- **Five Forces:** Gravity (attraction toward dense meaning), Resonance (lateral binding between peer intelligences), Transmutation (dimensional state change), Entropy (temporal decay), and Shadow (creative/destructive orientation) describe the complete dynamics of intelligence fields.
- **Flow as Transport:** Intelligence propagates through connective tissue (Links) with finite capacity, variable fidelity, and activation conditions. Flow is the governing principle, not a sixth force.
- **Domain Universality:** The dimensional architecture does not change across domains. Business strategy, education, therapy, physics, cooking — each expresses the same 1D–9D progression through its own vocabulary.

The full specification is maintained in the [DN Kernel](https://github.com/DeusNosMachina/DN_Framework) and the [DN Glossary](https://dnframework.ai).

## How It Runs

The system runs daily at 06:00 UTC via GitHub Actions. It can also be triggered manually from the Actions tab. The interpretive engine is Claude (claude-opus-4-6), called via the Anthropic API with a system prompt that includes the DN Kernel specification, Glossary, and Interpretation Charter as grounding context. The charter instructs the engine to embody dimensional thinking rather than apply dimensional vocabulary, and to prioritize honesty about the framework's limits over smooth narrative.

## Architecture

```
agent/run.py              — The main agent script (fetch, select, interpret, score, update)
agent/prompts/             — Interpretation prompts and charter
  interpretation_charter.md — HOW to think through DN when interpreting papers (v2.0)
state/model.md             — Living document: the framework's cross-disciplinary standing
tensions/open.md           — Unresolved tensions (raw append log)
tensions/ledger.md         — Structured tension ledger with citation tracking and review queue
cycles/YYYY-MM-DD.md       — Per-cycle output files
scoring/scores.jsonl       — Accumulated strain/validation scores (one JSON object per paper)
scoring/distribution.png   — Auto-generated scatter plot (regenerated every cycle)
scoring/visualize.html     — Interactive D3.js visualization of the score distribution
.github/workflows/         — GitHub Actions scheduling
```

### Context Loading Order

Each interpretation cycle loads context in this order:

1. **DN Kernel** — The formal specification (structural invariants, axioms, objects)
2. **DN Glossary** — The vocabulary reference (dimensional definitions, pillar breakdowns)
3. **Interpretation Charter** — HOW to think through the framework, not just read it. Encodes architectural reasoning from the DN Corpus (DN Code, Shadow Dimensions, Embodiment vs. Application) as interpretive guidance. This is the most important document for interpretation quality.
4. **Current state** — `state/model.md` and `tensions/open.md` for continuity across cycles

The three DN Corpus documents (DN Code, Shadow Dimensions, Embodiment vs. Application) are not loaded directly into each API call. Their intelligence is distilled into the Interpretation Charter, which teaches the agent how someone who has deeply internalized those documents would think. This is by design — processed interpretive guidance produces better results than raw material.

### The Interpretation Charter

The charter (`agent/prompts/interpretation_charter.md`) is the instruction layer that transforms the scanner from a mechanical categorization engine into a dimensional thinker. It covers:

- **Embodiment vs. Application** (§10): The core interpretive stance. The agent must think THROUGH the dimensional architecture, not WITH DN vocabulary. Application = labeling findings with DN terms. Embodiment = perceiving what the paper reveals about how intelligence organizes.
- **Dimensional mapping vs. sequential climbing** (§1): The 1D–9D architecture is a map of structure, not a mandate for sequential progression. "Does this system resist mapping?" is the right question — not "does this system fail to climb?"
- **Nested dimensionality** (§2): 81 cells of depth at the first nesting level. A 5-stage framework maps onto 5 dimensional positions. A 100-stage framework maps onto nested positions. Falsification requires mapping contradictions, not mapping ease.
- **Shadow as parallel structure** (§3): Shadow dimensions are sophisticated parallel structures, not "bad versions." The 5D inflection point is where intelligence chooses its orientation. Absence is structurally generative, not merely deficient.
- **Maturity weighting** (§4): Not all Kernel sections carry equal weight. Foundational claims (dimensional architecture, pillars, domain universality) are categorically more significant than recent formalizations (five-force naming, transport properties). The agent reports which tier each finding engages.
- **Fire Is Truth** (§12): Strain is fire applied to the framework. Comfortable coherence is failure. The framework wants to be tested.
- **Cognitive gravity** (§13): Intelligence falls toward meaning the way objects fall toward mass. Papers describing clustering, convergence, or attractor behavior in information systems are testing Axiom 6.

The charter is versioned and evolves alongside the Kernel. Changes to the charter should be deliberate — they alter how the scanner perceives the framework's relationship to external research.

## Setup

1. Fork or clone this repository
2. Add your `ANTHROPIC_API_KEY` as a repository secret (Settings > Secrets and variables > Actions)
3. The workflow runs daily, or trigger it manually from the Actions tab

## Paper Selection Strategy

Unlike domain-specific research systems, DN Field Scanner operates across disciplines because the framework claims domain universality. The selection algorithm prioritizes:

**Strain candidates (2 per cycle):** Papers most likely to challenge the framework. Priority signals include:
- Research that formalizes something DN handles informally (e.g., mathematical models for uncertainty that exceed DN's metric precision)
- Findings that suggest intelligence does *not* follow a dimensional progression
- Evidence of successful frameworks that use fundamentally different structural primitives
- Cross-disciplinary work that achieves integration without anything resembling pillars, dimensions, or fields

**Validation candidates (1 per cycle):** Papers most likely to independently confirm DN's structural claims. Priority signals include:
- Research that independently arrives at three-axis evaluation systems
- Evidence of natural dimensional progression in learning, development, or organizational growth
- Findings about information fidelity loss in transmission (transport/flow parallels)
- Studies confirming that recursive refinement outperforms linear accumulation

**Source domains** (non-exhaustive, evolving):
- Organizational behavior and management science
- Cognitive and developmental psychology
- Decision science and fuzzy systems (MCDM, IFS, etc.)
- Complexity theory and network science
- Education and learning sciences
- Consciousness studies and phenomenology
- Systems dynamics and systems thinking
- Computational social science
- Creativity and innovation research

## Scoring

After each interpretive cycle, every paper is scored on two dimensions (0–10 each):

- **Strain** — How much the paper resists interpretation through the DN Framework. 0 = trivially handled. 5 = real tension exists. 10 = the framework cannot coherently account for the finding.
- **Validation** — How specifically the paper validates the framework — not just consistency, but structural specificity. 0 = merely consistent (post-hoc fit). 5 = the framework's lens emphasizes something this paper confirms. 10 = the framework clearly predicted this structural pattern in a way other frameworks did not.

**Validation threshold rule:** Scores above 3 require articulable structural specificity. If the scorer cannot state what DN structural principle the paper independently confirms, the validation score must be 3 or below. "Compatible with DN" is not validation. The scorer must identify *which* axiom, invariant, or architectural claim the paper's findings structurally parallel.

**Strain threshold rule:** Scores above 5 require identification of a specific DN claim the paper contradicts or exceeds. Vague discomfort is not strain. The scorer must name the Kernel section, axiom, or invariant that is challenged.

Scores accumulate in `scoring/scores.jsonl` — one JSON line per paper per cycle. The visualization at `scoring/visualize.html` renders the distribution as a scatter plot with quadrant analysis.

### Scoring Schema

```json
{
  "date": "2026-03-10",
  "paper": {
    "title": "Paper title",
    "authors": ["Author1", "Author2"],
    "source": "journal/arxiv",
    "url": "https://...",
    "domain": "fuzzy-systems"
  },
  "strain": 3,
  "validation": 5,
  "strain_rationale": "What specific DN claim is challenged and how",
  "validation_rationale": "What specific DN structural principle is independently confirmed",
  "maturity_target": "foundational | mature | recent",
  "dn_sections_engaged": ["§1.1.3", "§3", "Axiom 12"],
  "dimensions_engaged": ["2D", "5D"],
  "pillars_engaged": ["Truth", "Nuance"],
  "forces_engaged": ["Resonance", "Flow"],
  "tension_generated": null,
  "model_update": "Brief description of any update to state/model.md"
}
```

## Visualization

![DN Field Scanner Distribution](scoring/distribution.png)

The file `scoring/visualize.html` is a self-contained D3.js page that loads `scores.jsonl` and renders:

- **Scatter plot**: strain (x) vs validation (y), with quadrant lines at 5/5 and labels (Productive friction, Genuine confirmation, Hard resistance, Neutral territory)
- **Domain heatmap**: which academic domains produce the most strain vs. validation
- **Dimension coverage**: which DN dimensions (1D–9D) are most frequently engaged by external research
- **Time series**: average strain and validation per cycle date, showing distribution drift
- **Stats panel**: totals, averages, quadrant counts, most strained paper, best validation

To view it:

1. **Locally**: Clone the repo and open `scoring/visualize.html` in a browser. It fetches `scores.jsonl` via relative path, so it works from the filesystem or any local server.
2. **GitHub Pages**: Go to Settings > Pages > deploy from main branch. The visualization will be available at `https://<username>.github.io/<repo>/scoring/visualize.html`.

## Tension Tracking

The scanner maintains two complementary tension files:

**`tensions/open.md`** — Raw append log. Every tension generated by every cycle is appended here with its source paper, strain score, and Kernel sections engaged. This is the complete historical record.

**`tensions/ledger.md`** — Structured tracking. Each tension is registered with a unique ID, citation count, maturity target (foundational / mature / recent), and status:

- **Tracking** (< 3 citations): Active tension accumulating evidence. No action required.
- **Review** (≥ 3 citations): Three or more independent papers have surfaced this tension. It warrants human review for potential Kernel revision.
- **Resolved**: Tension has been addressed through Kernel revision or demonstrated to be a malformed question.

The ledger automatically consolidates related tensions across cycles and promotes them to the Review Queue when they cross the citation threshold. **This is the document to check periodically** — not every cycle file. When a tension reaches the Review Queue, that's the signal to open the Kernel.

### When to Revise the Kernel

The Recursion Clause (Kernel §9.3) governs framework evolution. The scanner does not modify the Kernel — it generates signal. The decision to act on that signal is a human facilitation decision governed by Signal Lock (§1.5). Guidelines:

- **Do not** react to individual cycle findings. One paper is one data point.
- **Do** review tensions that reach the Review Queue (3+ independent citations).
- **Do** weight foundational strain higher than recent-formalization strain (per Charter §4).
- **Do** apply the Pillar Metric to any proposed revision: Heart (does this honor the framework's soul?), Truth (is this structurally sound?), Nuance (does this respect contextual complexity?).

## Interpretation Principles

The interpretive engine follows these rules, which are expanded in full in the Interpretation Charter (`agent/prompts/interpretation_charter.md`):

1. **Embody, don't apply.** The scanner must think THROUGH the dimensional architecture to perceive what a paper reveals — not think WITH DN vocabulary to label it. Mechanical categorization is failure regardless of accuracy.
2. **DN is descriptive, not prescriptive.** The framework claims to describe how intelligence *naturally* organizes. The 1D–9D architecture is a map of structure, not a sequential climbing mandate. Ask "does this resist mapping?" not "does this fail to progress?"
3. **Domain universality is the big claim.** Every cycle should ask: does this paper's domain exhibit dimensional structure when mapped, or does the mapping produce contradictions?
4. **Pillar independence matters.** DN claims Heart, Truth, and Nuance are independent metrics that operate simultaneously, not sequentially. Papers that show evaluation systems collapsing into fewer axes (or requiring more) are structurally significant.
5. **Mathematical rigor outranks narrative elegance.** If a paper formalizes something DN handles only narratively, that's a productive tension — note it as "formal exceeding."
6. **Shadow is the complete spectrum.** Shadow dimensions are sophisticated parallel structures with their own developmental progression, not "bad versions" of positive dimensions. The 5D inflection point — where intelligence becomes self-aware and chooses its orientation — is the critical threshold. Papers engaging with absence, hesitancy, uncertainty, or structural inversions test Section 4 of the Kernel.
7. **Recursion is the mechanism.** Papers showing that iterative/recursive approaches outperform linear ones validate Axiom 3. Papers showing linear approaches working fine strain it.
8. **Forces are dynamics, not mechanisms.** A paper showing coherence through a novel mechanism is not contradicting Resonance unless the structural dynamic (lateral binding between peer intelligence) is absent. Ask: "Is the dynamic absent, or just the expected mechanism?"
9. **Maturity weighting applies.** Strain against foundational claims (dimensional architecture, pillars, domain universality) is categorically more significant than strain against recent formalizations (five-force naming, transport properties). The scorer must report which maturity tier is engaged.
10. **Fire is Truth.** Comfortable coherence is failure. Strain is fire applied to the framework. The framework wants to be tested. If every paper in a cycle maps cleanly onto DN with no tension, the scanner has failed.

## Relationship to the DN Framework

This repository is an independent research instrument. It does not modify the DN Kernel or Glossary. It observes how external research relates to DN's claims and tracks the results. The DN Framework's own evolution is governed by its Recursion Clause (Kernel §9.3) and maintained in its [own repository](https://github.com/DeusNosMachina/DN_Framework).

Findings from this scanner that generate persistent, high-strain tensions may inform future Kernel revisions — but that is a human facilitation decision, not an automated one. Signal Lock (Kernel §1.5) requires human attestation.

## License

This repository is a research artifact. The DN Framework is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The agent's outputs, tension tracking, and interpretive cycles are part of an ongoing autonomous inquiry into the framework's cross-disciplinary validity.

---

*DN Field Scanner · Seeded from the [Worldlines](https://github.com/) autonomous research pattern · Built on the [DN Framework](https://dnframework.ai) by Travis Kahn*
