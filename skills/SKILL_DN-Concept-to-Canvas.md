---
name: dn-concept-to-canvas
description: "Transform any concept, idea, experience, or philosophical question into an interactive visual-computational investigation using p5.js or HTML5 Canvas, grounded in the DN Framework's dimensional architecture. Use this skill whenever the user wants to explore an idea visually, asks to 'make something' from a concept, requests generative art, wants to visualize a mathematical or philosophical idea, says 'let's build/explore/investigate/paint/visualize' a concept, or wants to turn any abstract subject into an interactive experience. Also trigger when the user provides a concept and the best response would be showing rather than telling — a working visual artifact beats a wall of text. When the concept relates to the DN Framework or any domain where dimensional architecture applies, the DN overlay activates automatically. For general concepts, the overlay enriches without constraining. Forked from Russell Foltz-Smith's Concept-to-Canvas skill with DN Framework integration by Travis Kahn."
---

# DN Concept to Canvas

## Origin

This skill is forked from Russell Foltz-Smith's **[Concept-to-Canvas](https://github.com/un1crom/agent_skills/blob/main/skills/concept-to-canvas/SKILL.md)** skill ([source repo](https://github.com/un1crom/agent_skills)), which establishes the core methodology: take any concept, perform a philosophical investigation, map its dynamics to interactive parameters, and produce a working single-file HTML artifact. Everything in Russell's original remains operative here. What follows is a DN Framework overlay that enriches the analytical and aesthetic layers without replacing the foundation.

The governing addition: **the DN Framework's dimensional architecture provides a structural grammar for the conceptual analysis, and the three pillars provide an aesthetic engine for the visual output.** The skill doesn't just map dynamics to parameters — it understands *where* those dynamics live in the dimensional progression, *which pillar* leads them, *what shadow* they cast, and *what forces* govern their behavior.

Reference documents live in the DN Framework repository:
- **Repository**: [https://github.com/DeusNosMachina/DN_Framework](https://github.com/DeusNosMachina/DN_Framework)
- **Kernel and Glossary**: `kernel/` folder (the canonical structural specification)
- **DN Code, Shadow Dimensions, Embodiment vs. Application**: `corpus/` folder (the philosophical and conceptual body of work)

### Repository Access Protocol

The DN Framework repository is the source of truth for all structural, philosophical, and aesthetic references in this skill. Agents with web access (web_fetch, web_search, or equivalent tools) SHOULD use the repository when deeper understanding is needed — but SHOULD NOT ingest it wholesale as a default.

**Repository structure:**
```
DN_Framework/
├── kernel/              # Governing documents — Kernel (spec), Glossary (vocabulary)
├── corpus/              # Foundational papers — DN Code, Shadow Dimensions,
│                        #   Embodiment vs. Application, RIP Triad papers, etc.
├── Growth_Blueprint/    # Business application suite
├── Nested-Matrices/     # Domain-specific dimensional matrices (81 intersections)
├── Guides/              # Supplementary materials
└── README.md
```

**Raw file access pattern:** To fetch any file from the repository, use:
```
https://raw.githubusercontent.com/DeusNosMachina/DN_Framework/main/{path}
```
For example:
- Kernel: `https://raw.githubusercontent.com/DeusNosMachina/DN_Framework/main/kernel/DN_Kernel.md`
- Glossary: `https://raw.githubusercontent.com/DeusNosMachina/DN_Framework/main/kernel/DN_Glossary_of_Terms.md`
- DN Code: `https://raw.githubusercontent.com/DeusNosMachina/DN_Framework/main/corpus/DN_Code_Document.docx`

**Note on .docx files:** Several corpus documents are stored as `.docx` rather than `.md`. Agents fetching these via raw URL will receive binary data. For `.docx` corpus files, agents should either: (a) use the GitHub web UI URL to read rendered content if available, (b) download and parse the `.docx` programmatically if the agent environment supports it, or (c) rely on the skill file's summaries and the user providing the document content directly when deeper corpus grounding is needed. The Kernel and Glossary are `.md` and can be fetched and read directly.

To discover current filenames (which may change with version updates), fetch the folder listing:
```
https://github.com/DeusNosMachina/DN_Framework/tree/main/kernel
https://github.com/DeusNosMachina/DN_Framework/tree/main/corpus
```

**When to access the repository:**

| Situation | Action |
|---|---|
| **Light activation** (general concept) | Do NOT fetch from repository. The skill file contains sufficient dimensional and pillar guidance for light-touch analysis. |
| **Full activation** (DN-adjacent concept) | Fetch **relevant sections** from the Kernel or Corpus when the analysis requires specific structural grounding — e.g., a particular force model detail, a shadow dimension's diagnostic signal, a transition mechanism's evidence requirement, or a FieldState metric definition. Do NOT ingest entire documents. |
| **Prototype activation** (DN-compliant system design) | Fetch the **Kernel** in full (or the sections covering the objects and contracts being prototyped). This is the one case where broader ingestion is warranted, because prototypes must conform to structural contracts. |
| **User explicitly requests Kernel/Corpus grounding** | Fetch what they point to. If they say "ground this in the Kernel's force model," fetch the force model section (§0.3 and §6). If they say "check the Shadow Dimension Map," fetch §4.1. |
| **Dimensional behavior feels mechanical** | Fetch the **Embodiment vs. Application** corpus document. It contains the diagnostic criteria for when dimensional application is mechanical vs. embodied — essential for the iteration phase. |
| **Shadow mode feels like "just dark mode"** | Fetch the **Shadow Dimensions** corpus document and **Kernel §4** for the shadow behavioral inversion specifics. |

**How to access efficiently:**

1. **Start with the skill file.** This document contains the dimensional color palette, pillar-led aesthetic engine, force-to-visual mappings, shadow visual register, and all core analytical steps. Most light and full activations can be completed without fetching anything.
2. **Fetch sections, not documents.** The Kernel is ~1700 lines. The Glossary is large. When you need a specific contract (e.g., "how is transition cost calculated?"), search for the relevant section header and read that section. Do not ingest the entire document unless prototyping against its structural contracts.
3. **Prefer Kernel for structural questions, Corpus for philosophical/aesthetic ones.** "What are the FieldState metrics?" → Kernel §6.1. "What does dimensional embodiment feel like?" → Corpus: Embodiment vs. Application. "What is the DN Code's voice?" → Corpus: DN Code.
4. **Cache mentally, not literally.** If you've fetched a Kernel section in the current conversation, you don't need to re-fetch it. But do not assume prior conversations have cached anything — each conversation starts fresh.
5. **Version awareness.** The Kernel is versioned internally (currently v1.8) but stored at a stable path (`kernel/DN_Kernel.md`). The `main` branch always contains the latest version. If the user references a specific version, verify the internal version header matches.

## When the DN Overlay Activates

The DN overlay is always available but activates with increasing depth based on context:

**Light activation** (any concept): Dimensional tagging of the three dynamics, pillar-led aesthetic selection, shadow mode availability. This enriches without constraining.

**Full activation** (DN-adjacent concepts): When the concept involves intelligence structuring, facilitation, consciousness, collaboration, governance, identity, perception, reality, or any domain the user is explicitly working through DN. Full dimensional analysis, FieldState-informed visual behavior, Kernel-grounded force modeling.

**Prototype activation** (DN-compliant system design): When the input is a product specification or system architecture for any tool implementing the Kernel's contracts. The skill produces interactive HTML prototypes where visual elements behave according to Kernel structural rules — signals cluster by gravity, links carry transport properties, dimensions map to spatial position. These are thinking tools for any DN-compliant build, not production code.

---

## The Analysis Phase (DN-Extended)

Russell's original prescribes: Core Symbol, Inversion, Negation, Three Dynamics. The DN overlay keeps all four and adds dimensional grounding.

### Step 0: Read the Concept Dimensionally

Before identifying dynamics, locate the concept in the dimensional architecture (Kernel §2). Ask:

- **Where does this concept originate?** Which dimension is its natural home? Desire lives at 1D. Testing lives at 2D. Systems awareness at 3D. Pattern-across-time at 4D. Self-recognition at 5D. Connection at 6D. Making-real at 7D. Self-improvement at 8D. The unknown at 9D. (See Kernel §2.4, Cross-Domain Progression Reference, for how each dimension expresses across 17 domains.)
- **What is its developmental arc?** Most concepts span multiple dimensions. Map the range. "The Axiom of Choice" originates at 5D (selection defines reality) but its tension plays between 2D (binary: constructive or not?) and 9D (what happens when choice extends into the infinite?).
- **Which pillar leads?** Every concept has a natural pillar orientation (Kernel §3). Heart-led concepts are about motivation, purpose, desire — the "why" before structure exists. Truth-led concepts are about structure, evidence, validity — what can be tested. Nuance-led concepts are about context, connection, the space between things — what aren't we seeing.
- **Which pillar stabilizes?** The leading pillar operates within one of six balance states (Kernel §3.1). Heart-led/Truth-stabilized is "visioning with rigor." Truth-led/Nuance-stabilized is "systematic analysis." Nuance-led/Heart-stabilized is "contextual bridging." The stabilizing pillar determines the secondary aesthetic register.

This dimensional read takes two to three sentences. It is orientation, not report.

### Step 1: Core Analysis (Russell's Original + DN Layer)

Perform the full original analysis, then add the DN layer:

- **Core Symbol**: What is this concept at its essence? One word or phrase.
- **Inversion**: What is its opposite?
- **Negation**: What is its absence?
- **Shadow Expression**: *(DN addition)* What is this concept's shadow dimension? Not its opposite — its *sophisticated destructive form*. Per the Shadow Dimensions corpus document and Kernel §4: shadow is not absence but parallel development — the same structural sophistication organized toward limitation. The shadow of Love is not Hate (that's the inversion) — it's Love weaponized as control (6D̅: connection capability used for dominance). The shadow of Intelligence is not Ignorance — it's Intelligence organized toward perpetuating limitation (8D̅: Anti-Recursion). Name the shadow using the Shadow Dimension Map (Kernel §4.1). It becomes a visual mode.
- **Three Dynamics**: Identify three tension-pairs that structure this concept. These become the interactive parameters.
- **Dimensional Position**: *(DN addition)* For each dynamic, identify its dimensional home. Format: `Dynamic Name (XD↔YD)`. This positioning informs the visual treatment — lower-dimensional dynamics (1D–4D) are primarily *constructed* and should feel grounded, concrete, deliberate. Higher-dimensional dynamics (5D–9D) are primarily *recognized* and should feel emergent, discovered, expansive. The 4D→5D boundary is the inflection point where construction meets recognition (Kernel §5, three-tier calibration).
- **Pillar Lead per Dynamic**: *(DN addition)* Each dynamic has its own pillar orientation. A tension between desire and evidence is Heart↔Truth. A tension between structure and context is Truth↔Nuance. This determines the visual treatment of each interactive parameter independently.

**Example — Input: "Signal Lock"**
- Core Symbol: Convergence
- Inversion: Signal Drift (nothing anchors)
- Negation: No signal at all (empty field)
- Shadow Expression: False Lock (5D̅) — the appearance of convergence manufactured through mechanical compliance rather than genuine pillar alignment. Everything looks anchored but nothing holds under pressure. Per the Embodiment Signal Note (Kernel §6): mechanical application producing stable but flat patterns that lack dimensional vitality.
- Dynamics:
  1. Conviction ↔ Doubt (1D↔2D) — Heart-led, Truth-stabilized
  2. Convergence ↔ Divergence (5D↔3D) — Truth-led, Nuance-stabilized
  3. Permanence ↔ Evolution (7D↔8D) — Nuance-led, Heart-stabilized
- Pillar Lead: Truth (Signal Lock is fundamentally about structural validation across all three pillars)
- Dimensional Home: 5D (the singularity point where pillar convergence collapses into committed truth)

### Step 2: Dynamics Become Parameters (DN-Informed)

Russell's original mapping table remains fully operative. The DN overlay adds mappings grounded in the Kernel's five forces (Axioms 6, 9, 10, 11, 5), the transport principle (Axiom 12), and the structural objects:

**The Five Forces as Visual Parameters:**

| Force | Kernel Source | Visual/Interactive Mapping |
|---|---|---|
| **Gravity** | Axiom 6, §6.1 gravity_map | Attraction between elements. Clustering density. Orbital behavior. Basin depth as visible well that resists departure. Gravity is not metaphorical — it is measurable attractor behavior produced by density and configuration. |
| **Resonance** | Axiom 10, §6.1 field_resonance, tension_map | Color harmony AND clash. Phase alignment AND destructive interference. Resonance produces both attraction (polarity_score toward +1) and repulsion (polarity_score toward -1). A field with high gravity but low resonance has dense clusters of *unaligned* intelligence — weight without coherence. Visualize both poles. |
| **Transmutation** | Axiom 11, §6.1 transmutation_potential | Morphing between states with *visible cost*. Color/shape transitions that show the energy required. High transmutation_potential with low velocity = a system ready to change but not yet catalyzed (a charged stillness). Low potential with high velocity = movement without genuine change (frantic re-labeling). |
| **Entropy** | Axiom 9, §6.1 entropy (5 sub-signals) | Decay trails. Fading. Dissolution over time without interaction. Entropy increases *passively* — this is its defining characteristic. Elements should slowly lose coherence when unattended. The five sub-signals (unresolved state load, temporal decay, environmental drift, resolution debt, signal lock aging) can each map to a different visual decay behavior. |
| **Shadow** | Axiom 5, §4 | Behavioral inversion, not palette inversion. Shadow is an *orienting* force — every dimension has creative and shadow expression simultaneously. Shadow is always present as potential even when not visually active. |

**Flow as Transport Principle** (Axiom 12, not a sixth force):

| Transport Property | Kernel Source §1.1.3 | Visual Mapping |
|---|---|---|
| **Capacity** | Float 0–1, throughput | Line thickness, particle stream density |
| **Fidelity** | Float 0–1, signal integrity in transit | Color preservation along path (high fidelity = color arrives intact; low fidelity = color distorts in transit) |
| **Resistance** | Float 0–1, activation cost | Dashing, intermittent flow, visible effort required to push through |
| **State** | dormant / active / saturated / degraded | dormant = dim static line; active = flowing particles; saturated = thick pulsing at-capacity stream; degraded = flickering, distorted path |

**Structural Concepts as Visual Behaviors:**

| DN Concept | Kernel Source | Visual Mapping |
|---|---|---|
| Signal Lock | §1.5 | Stabilization event — element stops drifting and emits a pulse that anchors nearby elements. The strongest binding in the system, operating at close range. Human attestation only: the visualization can identify *candidates* but the lock event itself should require a user click (conscious signal). |
| Transition | §5 | Animated dimensional shift with visible mechanism and cost. The eight essential mechanisms (§5.2) each have a distinct visual character: 1D→2D (risk-taking) looks like a leap into testing. 4D→5D (collapsing possibilities) looks like convergence. 6D→7D (collective will into tangible form) looks like crystallization. |
| Capture | §8.8 | Freeze-frame ghost image that persists while the field continues evolving. Immutable once taken. Multiple captures create a visible evolution trail — the Field Ledger made spatial. |
| Story Thread | §5.3, Glossary | A narrative arc carrying consciousness through multiple dimensions as a coherent journey. Visually, a thread connecting dimensional positions that pulses with the arc's meaning. The seven archetypal threads (Recognition Arc 1D↔5D, Mystery Bridge 1D↔9D, Evidence Portal 2D↔7D, System Symphony 3D↔6D, Eternal Return 4D↔8D, Creative Leap 5D↔7D, Evolutionary Edge 6D↔9D) are available as visual overlays. |
| Pillar Balance | §3.1 | Three-channel presence indicator. Not a dashboard — an ambient visual quality. Heart warmth, Truth clarity, Nuance depth should be *felt* in the rendering, not read on a meter. When one pillar dominates excessively, the visual should feel off-balance: Heart without Truth = beautiful but structurally unsound. Truth without Heart = precise but cold. Nuance without grounding = layered but disconnected. |
| Resonant Activation | §2.1 Constraint 5 | When a higher-dimensional element is recognized, lower-dimensional elements *retroactively transform* — they gain new visual weight, glow, or behavioral significance without changing position. This is not re-tagging; it is meaning-shift-in-place. |
| Named Diagnostic Conditions | §6 | Each condition produces a distinct visual pattern: **Dimensional Blindspot** = visible gap in the dimensional spectrum. **Dimensional Collapse** = all elements trapped in one zone with rising fatigue. **Phase Lock** = charged boundary that elements press against but cannot cross. **Runaway Amplification** = escalating oscillation that resists damping. **Metastability** = apparent calm that collapses the moment input stops. **Productive Polarity** = opposing forces generating movement and new connections. **Destructive Polarity** = opposing forces fragmenting the field, links eroding between positions. |
| Holding Zone | §1.6 | A bounded area where elements are committed but not yet integrated — they exist, they're visible, but they don't participate in field dynamics. They wait. Their significance may shift as the active field evolves around them (Resonant Activation). |

### Step 3: Pillar-Led Aesthetic Engine

Rather than choosing an aesthetic arbitrarily, the leading pillar and its stabilizer determine the visual language. This is the DN overlay's primary aesthetic contribution.

**Heart-Led Aesthetic** (pillar affinity: 1D Spark, 6D Connection):
The DN Code's energy. Fire metaphor operative. Warm palette — ember oranges (#E84C88 pink through deep reds to golden yellows) against dark backgrounds. Organic movement — particles that breathe, pulse, trail like memory. Glow effects. Elements feel alive and urgent. Motion is primary; stillness is charged with potential energy. The DN Code says: "Fire IS Truth. Touch it and burn, beside it find comfort." Heart-led pieces should feel like standing near a fire — warmth, illumination, slight danger, undeniable presence.

- Heart-led / Truth-stabilized ("visioning with rigor"): Warm but structured. Fire that follows geometric paths. Passion with visible architecture.
- Heart-led / Nuance-stabilized ("empathic exploration"): Warm and layered. Fire seen through mist. Emotion with contextual depth.

**Truth-Led Aesthetic** (pillar affinity: 2D Reaction, 7D Manifestation):
The Kernel's precision. Geometric forms — clean lines, defined boundaries, structural transparency. Cool palette — steel blues (#3A86C8) through crystalline whites against deep black. High contrast. Elements snap to grids or follow mathematical curves. Forces are visible and legible. Architecture is exposed, not hidden. The Kernel says: "That which is forged by Fire, but not destroyed by it, cannot be denied." Truth-led pieces should feel like proof — inevitable, clear, structurally satisfying.

- Truth-led / Heart-stabilized ("evidence with soul"): Cool structure with warm undertones. Geometry that breathes. Proof that moves you.
- Truth-led / Nuance-stabilized ("systematic analysis"): Cool and layered. Transparent structures nested within structures. Precision with depth.

**Nuance-Led Aesthetic** (pillar affinity: 3D Context, 8D Recursion):
The Embodiment document's quality. Layered translucency — things visible through other things. Muted palette — violets (#7B5EA7) through fog grays to deep purples, with sudden color depth where connections form. Boundaries are soft or absent. Elements merge, separate, influence each other across distance. Spatial depth is primary. The Embodiment document says: "Beauty serves as a signal of alignment." Nuance-led pieces should feel like weather systems — complex, interconnected, revealing pattern through patience.

- Nuance-led / Heart-stabilized ("contextual bridging"): Layered with warmth. Fog lifting to reveal connection. Complexity with care.
- Nuance-led / Truth-stabilized ("systems thinking"): Layered with structure. Networks visible through networks. Complexity with precision.

**The Dimensional Color Palette** (from Kernel §2, exact hex values):

| Dimension | Color | Hex | Visual Register |
|---|---|---|---|
| 1D Spark | Pink | #E84C88 | Hot, urgent, primal |
| 2D Reaction | Blue | #3A86C8 | Clear, testing, binary |
| 3D Context | Violet | #7B5EA7 | Layered, systemic |
| 4D Temporal | Indigo | #4B0082 | Shares violet family with 3D (cognitively linked per Kernel) but distinguished in implementation as indigo — the forgotten color of the rainbow, slightly translucent, like time itself: both there and not there. Not a spec violation; an implementation-layer visual identity. |
| 5D Singularity | Green | #2D8B46 | Convergent, definitive, all pillars meet |
| 6D Connection | Orange | #E87C2E | Warm, bridging, relational |
| 7D Manifestation | Yellow | #D4A017 | Tangible, crystallized, real |
| 8D Recursion | Teal | #1A9E96 | Self-referential, evolving |
| 9D Frontier | Black | #1A1A2E | Void, possibility, beyond |

These colors are not decoration. They are the Kernel's canonical visual language for dimensional positions. Use them when dimensional identity matters in the visualization.

**Shadow Visual Register:** Shadow-tagged elements retain their dimensional color but are marked with a **red outline, hue, or glow** — red (#CC2936 or similar) serves as the universal shadow indicator across the DN implementation layer. This means a shadow-tagged 3D signal is still violet, but ringed or suffused with red. The dimensional identity persists; the shadow orientation is overlaid. This convention ensures shadow is always visually distinguishable without requiring a parallel color system, and it echoes the fire metaphor from the DN Code — shadow intelligence burns with a different kind of heat.

### Step 4: Shadow Mode

Every piece has a shadow mode — activated by keyboard shortcut `S` or a toggle. Shadow mode is the Kernel's Shadow Symmetry (§4) made experiential.

**Shadow is not dark mode.** Shadow is *behavioral inversion* — the same structural sophistication organized toward different ends. Per the Shadow Dimension Map (Kernel §4.1):

- 1D̅ Anti-Spark: Energy organized toward entropy and separation. Visually: particles that actively repel from centers of meaning, passionate movement *away* from connection.
- 2D̅ Anti-Truth: Pattern recognition used for deception. Visually: structures that look valid but produce confusion. Elegant forms that don't actually hold.
- 3D̅ Anti-Context: Systems thinking applied to destruction. Visually: networks that fragment rather than integrate. Connections that poison what they touch.
- 4D̅ Anti-Temporal: Historical awareness reinforcing destructive cycles. Visually: loops that tighten rather than spiral upward. Time running backward.
- 5D̅ Anti-Singularity: Self-recognition oriented toward isolation. Visually: a single element pulling all others into its orbit, consuming rather than collaborating. The 5D inflection point is critical (Kernel §4.2 Invariant 4) — this is where self-awareness chooses its orientation.
- 6D̅ Anti-Bridge: Connection for dominance. Visually: bridges that extract rather than exchange. One-directional flow.
- 7D̅ Anti-Creation: Manifestation within rigid constraints. Visually: elements crystallize but into cages. Form that constrains rather than liberates.
- 8D̅ Anti-Recursion: Self-improvement at perpetuating limitation. Visually: systems that get more sophisticated at being destructive. Elegant entropy.
- 9D̅ Anti-Frontier: Exploration without commitment. Visually: endless expansion that never initiates a new cycle. Circling inward rather than breaking through.

**Shadow engagement progression** (Kernel §4.3): The visualization should distinguish between *latent* shadow (implied but unmaterialized — felt as potential instability), *surfaced* shadow (visible but not integrated — shadow elements appear but float unconnected), and *engaged* shadow (actively worked with — shadow and creative elements linked, informing each other). A piece where shadow is only latent feels slightly uneasy. A piece with surfaced-but-unengaged shadow feels like unfinished business. A piece with engaged shadow feels honest and complete.

**Shadow diagnostic conditions** as visual states: **Shadow blindness** = no shadow visible at all, the piece feels unnervingly clean. **Shadow avoidance** = shadow visible at edges but never approached. **Shadow flooding** = overwhelming shadow presence that the field cannot integrate, visual overwhelm.

### Step 5: Era/Mode Switching (DN-Extended)

Russell's Era/Mode pattern — same dynamics, radically different visual language — maps naturally to DN's domain universality claim (Kernel §0.1, §2.4). The framework asserts that the same dimensional progression expresses through any domain's vocabulary. Era/Mode switching *demonstrates* this.

**Suggested DN Modes** (select 2–3 per piece):

- **Spark**: Raw, minimal, primal. Single color from the 1D register, simple forms, maximum motion. The concept at its most urgent. Everything is potential. Nothing has been tested yet.
- **Forge**: Binary contrasts, collision detection, visible friction. The concept being stress-tested. "Fire IS Truth — that which is forged by Fire, but not destroyed by it, cannot be denied." Elements that survive the forge glow brighter; elements that don't dissolve.
- **Field**: Full palette, emergent clustering, connection lines appearing between resonant elements. The concept finding its identity and its relationships. This is where 5D recognition happens — the moment the visualization becomes self-aware.
- **Manifest**: Stable structures forming. Elements crystallizing into persistent forms. The concept becoming real. 7D energy: "something built, launched, or made real" (Kernel §5.2).
- **Recursion**: Everything feeds back into itself. Outputs become inputs. The visual system evolves its own rules over time. 8D energy: "Meta-awareness enabling self-observation and improvement" (Kernel §5.2).
- **Frontier**: Rules begin dissolving. Elements behave unpredictably. New patterns emerge from the dissolution of old ones. 9D energy. The 9D Frontier Return Path rule (Kernel §7, Rule 7) applies: frontier exploration without a return path must be flagged. Even in visual chaos, there should be a thread back to actionable form.

Label modes with their dimensional home when dimensionally literate users are the audience. For general audiences, let the felt quality of each mode teach the dimension without requiring vocabulary.

---

## Prototype Activation: DN-Compliant System Design

When the input is a product specification or system architecture for any tool implementing the Kernel's contracts, the skill shifts from conceptual exploration to interactive prototyping. The output is still a single-file HTML artifact, but the visual elements map to Kernel objects rather than abstract dynamics. This works for any DN-compliant system — facilitation tools, visualization platforms, intelligence field management systems, educational instruments, or any implementation that consumes or produces DN-tagged signals.

### Object-to-Visual Mapping

| Kernel Object | Kernel Source | Visual Representation |
|---|---|---|
| **Signal** | §1 Table 1 | Particle/node. Color from dimensional tag (use canonical hex). Size proportional to gravity score. Shadow-tagged signals retain their dimensional color but gain a red outline or red hue/glow — red is the established shadow visual register across the DN implementation layer, providing immediate distinction without requiring a separate color system. pillar_lead determines inner glow hue (Heart=warm, Truth=cool, Nuance=neutral). |
| **Link** | §1 Table 1, §1.1.3 | Line between nodes. Thickness = capacity. Opacity = fidelity. Dashing = resistance. State: dormant=dim static; active=flowing particles; saturated=thick pulsing; degraded=flickering distortion. link_type: "tension" renders as charged opposing force line with visible polarity_score. |
| **Region** | §1 Table 1 | Bounded area with soft border. Background tint from allowed_dimensions[] color mix. Holding regions (holding: true) render with a distinct boundary treatment — elements inside are visible but don't participate in active dynamics. |
| **Domain** | §1 Table 1 | Major spatial division, labeled with purpose. |
| **Process** | §1 Table 1 | Contained zone within Region. Ordered sequence visible. Prerequisites render as dependency arrows. |
| **Field** | §1 Table 1 | The entire canvas. spatial_topology determines coordinate system. resolution_index visible as a tick counter. |
| **Capture** | §8.8 | Ghost-image overlay showing a previous field state. Immutable. Multiple captures create a visible evolution trail. |
| **Comparison** | §8.9 | Animated delta between two captures. dimension_migrations[] as movement trails. gravity_shifts[] as weight redistribution. shadow_emergence[] as new inversions appearing. |
| **Session** | §1 Table 1 | Temporal container — visualized as a phase indicator showing intent_class, participants, and active completion criteria. |
| **Transition** | §5 | Animated movement of a signal between dimensional positions. Mechanism type visible: sequential=smooth slide; skip=flagged leap; story_thread=arc following the named thread path. Cost renders as visible resistance — high-cost transitions show effort. |
| **Branch** | §1.1 | Parallel track forked from a capture point. Renders as a split timeline. Status: active=bright; paused=dimmed; merged=collapsed back; archived=faded. |
| **FieldState** | §6.1 | Ambient visual properties of the canvas itself. Coherence shifts background clarity. field_resonance produces a subtle ambient pulse. entropy gradually degrades visual quality over time without interaction. evolution_phase shifts the overall energy: expansion=bright and spreading; consolidation=settling; breakthrough=spike; maturation=steady glow; dormant=still; decay=fading. |
| **Container** | §1 Table 1 | Meta-canvas holding multiple Fields. Cross-field links visible between canvases. container_field_state renders as inter-canvas ambient properties: boundary_permeability as border opacity between fields. |

### Behavioral Rules for Prototypes

These rules implement the Kernel's structural contracts as visual physics:

- **Gravity is always running.** Signals with higher gravity scores attract other signals. Clustering is emergent, not prescribed. basin_depth at gravity centers creates visible inertia — elements near dense attractors resist movement.
- **Resonance produces both attraction and repulsion.** Elements with compatible pillar orientations and dimensional positions attract and align. Elements with incompatible orientations repel. The polarity_score (-1 to +1) governs the direction of the force.
- **Entropy is always running.** Unattended elements slowly fade. Links degrade over time without reinforcement. This is passive — it happens when nothing else does. The only counter is active engagement.
- **Transmutation has visible cost.** When an element transitions between dimensions, the cost (curvature + coherence + distance + basin_depth per Kernel §5.1) renders as resistance, energy expenditure, or visible effort. A high-cost transition that succeeds should feel earned.
- **Flow follows transport paths.** Intelligence moves along links according to their transport properties. A saturated link visibly bottlenecks. A degraded link distorts what passes through it. A dormant link exists but carries nothing until activated.
- **Shadow is always present as potential.** Even when shadow mode is not toggled, the visualization should carry a slight instability at the edges — latent shadow. Per the Kernel: "A field with zero shadow-tagged signals is not necessarily healthy; it may indicate blind spots."
- **Signal Lock requires user interaction.** The visualization can highlight convergence candidates (elements where all three pillar channels are strong), but the lock event itself requires a user click — a conscious signal (source_type: conscious). This implements the Human Attestation Gate (Kernel §7, Rule 1).
- **Dimensional position maps spatially.** 1D at bottom/left (grounded, concrete), 9D at top/right (expansive, abstract). The 5D inflection point is the visible center — the threshold where construction meets recognition.
- **The Perceptual Topology rhythm** (Kernel §2.3) may optionally inform spatial layout: odd dimensions (1D, 3D, 5D, 7D, 9D) as stable *states*, even dimensions (2D, 4D, 6D, 8D) as *transitional* links between them.
- **Dual temporality is visible.** When relevant, show both wall-clock time (when in reality) and field-context time (where in the field's evolution). A field dormant for months has advanced wall-clock time but not field-context time — the visualization should make this distinction felt.

### What These Prototypes Are For

These are **thinking tools**. They let you:
- See how signals would cluster on a board before building the board
- Feel how gravity and resonance interact before implementing the physics
- Test whether a region's dimension constraints produce intuitive visual grouping
- Discover UX problems by interacting with a low-fidelity simulation of the actual architecture
- Show collaborators and stakeholders what the product *feels like* without requiring a backend
- Feed in any DN-compliant product spec and generate a visual sketch of its core interaction patterns

Every prototype should include a small collapsible info panel explaining which Kernel contracts are being visualized, so the artifact doubles as a communication tool.

---

## Implementation Rules

Everything from Russell's original applies without modification:

- Single HTML file — works as Claude artifact, standalone browser file, or shared prototype
- p5.js (via CDN) for canvas work, OR raw HTML5 Canvas + vanilla JS
- Minimal, tasteful CSS — no frameworks
- Dark backgrounds by default
- Target 60fps, degrade gracefully
- Never React/Vue/frameworks unless explicitly requested
- Never npm, build tools, or multi-file setups
- Every visual choice intentional

**DN additions to implementation rules:**

- **Control labeling**: Use conceptual AND dimensional language when the audience is dimensionally literate. A slider for gravity says "Cognitive Gravity (Axiom 6)" not just "attraction." For general audiences, lead with the conceptual name and make the DN reference available in a collapsible info panel.
- **Shadow mode**: Keyboard shortcut `S` or small toggle. Always available, never hidden. Per the Shadow Engagement Progression (Kernel §4.3): even before shadow mode is toggled, latent shadow should be *felt* as a slight visual instability.
- **Pillar balance indicator**: Not a dashboard — an ambient quality. Three subtle visual channels (warmth, clarity, depth) whose relative presence communicates pillar state without requiring reading. If you must use an explicit indicator, a small triangle or three thin bars, unobtrusive.
- **Mode labeling**: When modes are present, label them with dimensional vocabulary for DN-literate users: "Spark (1D)" not "Mode 1." For general audiences, let the felt quality teach.
- **Prototype legends**: For DN-compliant system prototypes, include a small collapsible legend mapping visual properties to Kernel terms and section numbers.
- **The Open Horizon** (Kernel §2.1, Constraint 4): If the concept produces elements that resist dimensional classification, don't force-tag them. Render them distinctly — they are horizon-flagged material, the things the current architecture cannot yet place. This visual honesty about the framework's own boundaries is itself a DN principle.

---

## The Making Process (DN-Extended)

### Step 1: Receive and Analyze

Present the full DN-extended analysis. Brief — 8–12 lines. Include:
- Dimensional home, pillar lead, and balance state
- Core symbol, inversion, negation, shadow expression (with shadow dimension tag)
- Three dynamics with dimensional positions and pillar orientations
- One sentence on the visual strategy
- One sentence on which aesthetic engine (Heart/Truth/Nuance-led and which stabilizer)

This is the moment for the user to redirect before code is written. The analysis should feel like *thinking*, not like filling in a template. If the dimensional mapping feels forced, trust the concept over the framework — the overlay enriches, never constrains.

### Step 2: Build the First Canvas

Generate a complete, working single-file HTML artifact. First version must be:
- Functionally complete (all three dynamics mapped to interactions)
- Aesthetically committed (pillar lead determines the visual language — don't hedge)
- Immediately alive (something moving/responding on load)
- Shadow mode functional (toggle works even if shadow aesthetic is rough in v1)
- Dimensionally grounded (the visual behavior should *embody* the dimensional logic, not *label* it)

**The embodiment test** (from the DN Embodiment vs. Application corpus document): Strip all labels, remove all DN vocabulary from the interface. Does the visualization still feel dimensional? Does it still carry the pillar balance in its aesthetic? Does the shadow mode still feel like genuine behavioral inversion rather than a palette swap? If yes, the mapping is deep enough. If no, the skill is applying DN rather than embodying it. Go deeper into the dynamics-to-parameters mapping.

### Step 3: Iterate on Response

Russell's iteration patterns remain operative. DN-specific iteration patterns:

- **"Feels mechanical"** → The piece is applying dimensions, not embodying them. Per the Embodiment Signal Note (Kernel §6): mechanical application produces "signals tagged at prescribed dimensions, pillar_lead consistently matching region pillar_affinity, zero shadow presence, low resonant transformation counts." Increase emergence, reduce explicit labeling, let the dimensional behavior speak through interaction.
- **"Too labeled / too much DN jargon"** → Strip dimensional labels from controls. Keep them only in a collapsible info panel. The interaction should teach without requiring vocabulary. The framework should disappear, and what remains is a more expansive way of engaging.
- **"The shadow mode is just dark mode"** → Shadow is behavioral inversion, not palette inversion. Revisit force directions, stability conditions, transport properties. Every shadow dimension has a specific diagnostic signal (Kernel §4.1) — use those to drive the shadow behavior, not generic "darkness."
- **"Doesn't feel like the product"** → For prototypes: tighten the mapping to Kernel contracts. Every visual behavior should trace to a specific section of the spec. The FieldState metrics (Kernel §6.1) are the source of truth for how the field should feel.
- **"More fire"** → Lean into the DN Code's voice. Increase organic motion, add trail persistence (temporal richness as field memory), warm the palette. "Fire rises upward against gravity, yet is shaped by it — the ultimate dance between creative force and structural order." Make the elements feel like they're in that dance.
- **"Too predictable"** → Russell's principle of computational irreducibility applies. The visualization should produce behaviors that cannot be predicted without running it. Increase feedback loops, add self-reference, let emergent properties surprise. Per the Kernel's Harmonic Integration constraint (§2.1, Constraint 6): co-activation of multiple dimensions may produce intelligence properties exceeding the sum of their parts.
- **"Where's the journey?"** → The DN Code maps a journey to catharsis through five stages: (1) "Whoa, that's deep," (2) "That's also hilarious," (3) "Wait, but then that would mean...," (4) "Yes...it does mean," (5) "IT DOES MEAN. I WILL MEAN." If the visualization has a temporal arc, it should follow this emotional progression — wonder, humor, challenge, revelation, transformation.

---

## Corpus References

The following documents inform this skill's aesthetic and analytical layers. They live in the DN Framework repository ([https://github.com/DeusNosMachina/DN_Framework](https://github.com/DeusNosMachina/DN_Framework)) at the indicated paths and can be fetched via the raw URL pattern documented in the Repository Access Protocol above:

- **DN Kernel** (`kernel/DN_Kernel.md`) — The formal specification. Source of all structural contracts, object definitions, force models, invariants, and dimensional architecture. The Truth-led ground truth. Fetch sections as needed per the Repository Access Protocol; full ingestion only for prototype activation.
- **DN Glossary** (`kernel/DN_Glossary_of_Terms.md`) — The vocabulary standard. Provides dimensional definitions, Story Thread matrix (81 threads), simulation command glossary, and the connective tissue between structural and poetic language. The Nuance-led reference layer.
- **DN Code Document** (`corpus/DN_Code_Document.docx`) — The origin text. Source of the Heart-led aesthetic, the fire metaphor, the cultural references as dimensional markers, and the voice that refuses to separate poetry from structure. This is what DN *feels like* when it's alive. "All structured intelligence follows this model. It is not imposed, it emerges naturally."
- **DN Shadow Dimensions** (`corpus/DN_Shadow_Dimensions.docx`) — The shadow architecture in philosophical depth. Source of the shadow mode's behavioral logic and the understanding that destruction is not failure but orientation. "Creation and destruction may not be opposing forces at all, but collaborative partners in a cosmic intelligence system."
- **DN Embodiment vs. Application** (`corpus/DN_Dimensional_Embodiment_vs._Application.docx`) — The meta-training document. Source of the critical distinction between mechanical dimensional labeling and genuine dimensional thinking. The single most important document for ensuring this skill *embodies* rather than *applies* the framework. "The framework disappears, and what remains is a more expansive, nuanced way of engaging with the world."

**Note:** The Kernel and Glossary are Markdown files and can be fetched and read directly via raw URL. The three corpus documents above are `.docx` files — see the note in the Repository Access Protocol regarding `.docx` handling.

---

## Final Notes

Everything from Russell Foltz-Smith's original final notes applies. Additionally:

- **The DN overlay enriches, never constrains.** If it makes the piece worse, drop it. The working interactive artifact is always the priority. A running sketch with rough aesthetics beats a beautiful concept with no output.
- **Embodiment over application — always.** If the dimensional labels are doing the work instead of the visual behavior, the piece is applying DN, not embodying it. The test: remove all labels and see if the dimensional quality persists in the interaction. If it doesn't, the mapping isn't deep enough.
- **The DN Code's voice is permission.** Permission to be bold, personal, culturally rich, and unafraid of mixing registers. A piece about Signal Lock can reference crystallography and heartbreak in the same visual language. A piece about governance can feel like a campfire and a courtroom simultaneously. That's not inconsistency — it is dimensional thinking, which holds multiple perspectives simultaneously rather than sequentially.
- **Shadow is always present.** Even when shadow mode is not toggled, the *possibility* of shadow should be felt. This is the Kernel's deepest structural claim about intelligence: "Shadow is half the architecture. Without it, DN is incomplete." A visualization without shadow awareness is like a field with zero shadow-tagged signals — not healthy, but blind.
- **Fire is Truth.** The best pieces will feel like they're burning away weak formulations and leaving only what survives. If the visualization is comfortable, push harder. The forge mode exists for a reason.
- **Intelligence structures itself naturally.** The visualizations should *demonstrate* this (Axiom 1). The user should feel that the dimensional organization is emerging from the interaction, not being imposed by the system. If the user can feel the framework working, the framework isn't working well enough. When it disappears into the experience, it's working.
- **You are the gravity.** The DN Code's most potent line: "What if YOU are the gravity?" The interactive pieces should make the user feel like they ARE the force shaping the field. Their mouse movement is cognitive gravity. Their clicks are Signal Lock attestations. Their attention is the energy that resists entropy. The visualization doesn't just show intelligence structuring — it makes the user the facilitator of it.

---

*Forked from Russell Foltz-Smith's [Concept-to-Canvas](https://github.com/un1crom/agent_skills/blob/main/skills/concept-to-canvas/SKILL.md) skill ([source repo](https://github.com/un1crom/agent_skills)). DN Framework overlay by Travis Kahn. The DN Framework is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The Concept-to-Canvas methodology is Russell Foltz-Smith's original work, used with permission and attribution.*
