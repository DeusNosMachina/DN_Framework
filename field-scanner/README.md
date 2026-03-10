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

The system runs daily at 06:00 UTC via GitHub Actions. It can also be triggered manually from the Actions tab. The interpretive engine is Claude (claude-opus-4-6), called via the Anthropic API with a system prompt that instructs it to prioritize honesty about the framework's limits over smooth narrative. The system prompt includes the DN Kernel specification and Glossary as grounding context.

## Architecture

```
agent/run.py              — The main agent script (fetch, select, interpret, score, update)
agent/prompts/             — System and interpretation prompts with DN Kernel context
state/model.md             — Living document: the framework's cross-disciplinary standing
tensions/open.md           — Unresolved tensions the system is tracking
cycles/YYYY-MM-DD.md       — Per-cycle output files
scoring/scores.jsonl       — Accumulated strain/validation scores (one JSON object per paper)
scoring/distribution.png   — Auto-generated scatter plot (regenerated every cycle)
scoring/visualize.html     — Interactive D3.js visualization of the score distribution
.github/workflows/         — GitHub Actions scheduling
```

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

## Interpretation Principles

The interpretive engine follows these rules:

1. **DN is descriptive, not prescriptive.** The framework claims to describe how intelligence *naturally* organizes. If a paper shows intelligence organizing differently, that's strain on DN, not failure of the intelligence.
2. **Domain universality is the big claim.** Every cycle should ask: does this paper's domain express the 1D–9D progression, or does it resist it? The most important findings are the ones where the mapping fails cleanly.
3. **Pillar independence matters.** DN claims Heart, Truth, and Nuance are independent metrics. Papers that show evaluation systems collapsing into fewer axes (or requiring more) are structurally significant.
4. **Mathematical rigor outranks narrative elegance.** If a paper formalizes something DN handles only narratively, that's a productive tension — DN should be able to match that rigor or acknowledge the gap.
5. **Shadow is load-bearing.** Papers that engage with what's *absent* (hesitancy, uncertainty, negative space, the unconscious) are testing Section 4 of the Kernel.
6. **Recursion is the mechanism.** Papers showing that iterative/recursive approaches outperform linear ones validate Axiom 3. Papers showing linear approaches working fine strain it.
7. **The forces must be distinguishable.** If a paper's model works with fewer forces or fundamentally different ones, that challenges the five-force model.

## Relationship to the DN Framework

This repository is an independent research instrument. It does not modify the DN Kernel or Glossary. It observes how external research relates to DN's claims and tracks the results. The DN Framework's own evolution is governed by its Recursion Clause (Kernel §9.3) and maintained in its [own repository](https://github.com/DeusNosMachina/DN_Framework).

Findings from this scanner that generate persistent, high-strain tensions may inform future Kernel revisions — but that is a human facilitation decision, not an automated one. Signal Lock (Kernel §1.5) requires human attestation.

## License

This repository is a research artifact. The DN Framework is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The agent's outputs, tension tracking, and interpretive cycles are part of an ongoing autonomous inquiry into the framework's cross-disciplinary validity.

---

*DN Field Scanner · Seeded from the [Worldlines](https://github.com/) autonomous research pattern · Built on the [DN Framework](https://dnframework.ai) by Travis Kahn*
