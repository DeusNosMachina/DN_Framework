# DN Kernel — Changelog

**Repository:** [github.com/DeusNosMachina/DN_Framework](https://github.com/DeusNosMachina/DN_Framework)

This file contains the complete version history for the DN Kernel specification. The current kernel document (DN_Kernel_v12.md) carries only the latest version's summary in Section 0.2. This file preserves the full record.

---

## v1.3 (February 2026)

**Source:** Self-audit of DN Kernel v1.2 against Glossary and Changelog identified 17 findings across structural, inconsistency, and advisory severity tiers. Core architecture validated as sound — problems existed at layer boundaries, not in the architecture itself.

**JSON schema key universalization:**

- Universalized all JSON schema keys in Section 8 from pre-v1.0 implementation terms to kernel terms. The v1.2 vocabulary pass universalized prose and JSON value-level scope fields but explicitly protected JSON keys as "implementation-layer identifiers." The self-audit found that developers copy examples, not prose — divergent key naming between examples and prose descriptions would produce incompatible implementations. All §8.1–§8.15 schema examples now use kernel-term keys: board_id → field_id, artifact_id → signal_id, bridge_type → link_type, snapshot_ids → capture_ids, zone_id → region_id, exercise_id → process_id, workspace_id → container_id, sections → domains, zones → regions, exercises → processes, artifacts → signals. ID prefixes updated accordingly (art_ → sig_, board_ → field_, snap_ → cap_, ex_ → proc_, bridge_ → link_, ws_ → ctr_, sec_ → dom_, zone_ → reg_, dod_ → cc_). The §0.4 vocabulary mapping table continues to document the implementation aliases for application layers that use original product terminology.

**FieldState stub completion:**

- Added missing load-bearing metrics to the Field Export FieldState stub (Section 8.2): entropy (Axiom 9, triggers decay phase), dimensional_coherence (per-dimension coherence breakdown), field_resonance (harmonic integration strength), gravity_map, tension_map, and evolution_breadth. The v1.1 stub addition included coherence, drift, saturation, fatigue, and evolution metrics but omitted these five, all of which are defined in §6.1 and referenced by simulation contracts.

**Axiom misattribution fix:**

- Fixed Force Model Note (Section 0.3): Shadow was cited as Axiom 4 (Fire/Testing); corrected to Axiom 5 (Shadow/Orientation). Constitutional reference integrity restored.

**Table 1 fix:**

- Fixed Field required properties in Table 1: sections[] → domains[]. The v1.0 vocabulary pass renamed the prose description but missed the canonical required-properties list.

**Transition model reconciliation:**

- Reconciled three-tier transition model constraint (Section 5.3) to match Section 5 preamble. §5 preamble defined three tiers: 1D→3D (constructed), 4D→5D (hybrid), 6D→9D (recognized). §5.3 constraint contradicted with two tiers: 1D→4D (created), 5D→9D (recognized). §5.3 now matches the authoritative three-tier model, and the constraint text reflects the hybrid middle tier.

**Completion criteria status enum placement:**

- Added the seven-value completion_criteria status enum (met | partially_met | unmet | deferred | scope_changed | not_evaluated | open_exploration) to the Section 1.6 structural requirement where completion criteria are first defined. Previously the enum appeared only in Session schema prose (§8.10). The structural requirement now documents the enum at its definitional home.

**Changelog translation note:**

- Added vocabulary translation note after the v0.9 changelog entry mapping pre-v1.0 terms to current kernel terms for readers tracing architectural decisions through historical entries.

**Glossary conformance (parenthetical clarification):**

- Added parenthetical kernel-term clarifications to Glossary entries that use application-layer vocabulary, conforming Glossary definitions to kernel terminology without duplicating the kernel's term definitions. The Glossary intentionally does not re-list kernel terms as separate entries to avoid version drift between documents.

**Structural impact:** All §8 JSON schema examples universalized (12 schemas, ~45 key replacements). 5 missing FieldState metrics added to Field Export stub. 1 axiom reference corrected. 1 Table 1 property corrected. 1 transition model constraint reconciled. 1 status enum relocated to definitional home. Glossary parenthetical conformance pass. No existing axioms, invariants, constraints, or behavioral rules modified. All changes are corrective and normalizing.

---

## v1.2 (February 2026)

**Source:** External audit (Grok) of DN Kernel v1.1 identified structural gaps in serialization schema coverage, simulation output contract precision, and transition pathway typing. Prioritized by distinguishing genuine schema gaps from layer-confusion misreads (where the auditor expected the Kernel to perform implementation-layer enforcement).

**Missing serialization schemas:**

- Added Section 8.13 (Transition Schema). The minimum viable JSON representation of a DN Transition, including all fields from the Transition interface (Section 5.1): id, subject_id, from_dim, to_dim, mechanism, mechanism_type, story_thread_id, barrier, evidence, pillar_lead, timestamp, cost, cost_factors. Includes documentation of evidence calibration requirements across the three-tier model (constructed, hybrid, recognition). This was the highest-priority gap: Transitions are referenced by Evolution Tracking (Section 1.1.1), Comparisons (Section 8.9), and every simulation command, but had no export/import contract.
- Added Section 8.14 (SimulationRun Schema). The minimum viable JSON representation of a DN SimulationRun, including: id, command, scope_ids[], input_state, output_state, pillar_balance, signals_produced[], transitions_produced[], session_id, timestamp. Establishes the provenance contract for all simulation-derived intelligence (source_type: simulation per Section 1.2). Mirrors the signal_lock_candidates[] distinction (see below) in output_state.
- Added Section 8.15 (Environment Schema). The minimum viable JSON representation of a DN Environment — the outermost containment boundary. Includes: id, name, description, container_ids[], tenant_isolation, created_at, updated_at, metadata{}. Explicitly documents that Environment is an administrative boundary, not an intelligence field: it carries no FieldState, spatial_topology, or position. Cross-Environment interaction is not defined by this Kernel.

**Signal Lock candidate distinction:**

- Fixed Generate Resonance Result contract (Section 7.2) to output `signal_lock_candidates[]` rather than `signal_locks[]`. The original naming implied the simulation applied Signal Lock, violating the Signal Lock Invariant (Section 1.5) which requires human attestation. The fix enforces the epistemic distinction at the contract level: simulations identify candidates; humans attest locks. SimulationRun schema (Section 8.14) mirrors this naming in output_state.

**Transition pathway typing:**

- Added `mechanism_type` enum (sequential | skip | story_thread) and `story_thread_id` (nullable) to the Transition interface (Section 5.1) and Transition required properties in Table 1 (Core Objects). This enables typed classification of transition pathways: sequential for adjacent dimensions, skip for non-adjacent (flagged for review against dimensional_coherence), and story_thread for named narrative arcs. When mechanism_type is story_thread, story_thread_id identifies the specific arc. Templates may define domain-specific Story Thread ids beyond the seven archetypes documented in the corpus layer. Updated Transition Schema (Section 8.13) to include both fields.

**Holding Zone explicit identification:**

- Added `holding` boolean (default: false) to Region required properties in Table 1 (Core Objects). When true, the Region is a Holding Zone per Section 1.6: its signals are operationally excluded from active field operations and FieldState computation. Updated Section 1.6 (Holding Zone) to explicitly reference the `holding` flag as the structural marker for filtering, cross-referencing Table 1, FieldState (Section 6.1), Field Export (Section 8.2), and Capture (Section 8.8). DN-compliant systems MUST filter signals in Regions where `holding: true` from FieldState metric inputs. Implementation layers no longer need to rely on naming conventions.

**Signal Lock candidate enforcement (additional):**

- Fixed Create Storyfield command (Section 7.1) to output `signal_lock_candidate: boolean` rather than `signal_lock: boolean` in storyfield_trace[] entries. Updated constraint to clarify that simulation-identified candidates require human attestation per Section 1.5. All simulation output contracts now consistently use candidate terminology.

**Vocabulary universalization completion:**

- Completed the v1.0 vocabulary universalization pass. Swept all remaining implementation-specific terms from kernel prose: "artifact" → Signal, "bridge" → Link, "zone" → Region, "board" → Field, "exercise" → Process. 92 prose-level replacements across axioms (Section 0.3), signal sources (Section 1.2), provenance groups (Section 1.3), external simulation provenance (Section 1.4), Signal Lock (Section 1.5), facilitation contract (Section 1.6), dimensional constraints (Section 2.1), shadow engagement (Section 4.3), transition constraints (Section 5.3), field health metrics (Section 6), FieldState (Section 6.1), simulation contracts (Section 7.1, 7.2), serialization schemas (Section 8), and field-to-field dynamics (Section 10). JSON value-level scope fields updated from implementation terms ("intra-board", "cross-board") to kernel terms ("intra-field", "cross-field") in Comparison (Section 8.9) and Container (Section 8.12) schema examples. Renamed "TENSION BRIDGE TYPE" header to "TENSION LINK TYPE" (Section 1.1). All protected content unchanged: JSON schema keys (implementation-layer identifiers like "artifact_id", "bridge_type"), §0.4 vocabulary mapping table (implementation aliases by design), product names ("Blueprint Board"), proper names ("Love Bridge", "Anti-Bridge", "Mystery Bridge", "Holding Zone"), dimension names, simulation command names, and Story Thread names.

**Structural impact:** 3 new serialization schemas (§8.13, §8.14, §8.15), 2 new Transition fields (mechanism_type, story_thread_id), 2 simulation contract fixes (signal_lock_candidates in §7.1 and §7.2), 1 new Region property (holding) wired to operational rules (§1.6), vocabulary universalization completion (92 prose-level replacements, 4 JSON value-level scope fixes). No existing axioms, invariants, constraints, or behavioral rules modified. All changes close gaps identified by external audit — no new architecture introduced. Additive, corrective, and normalizing.

---

## v1.1 (February 2026)

**Source:** Late-night architectural recognition — the Kernel's objects carry dimensional coordinates (what kind of intelligence) but not spatial coordinates (where the intelligence sits within the bounded space of a Field). The 9×9×9 nested dimensional matrix is an 81-point map viewed from a 9-dimensional lens — but navigated through physical space. Every interface layer, from a flat whiteboard to a holographic volume, is a spatial topology within which the dimensional architecture renders. The piping was missing.

**Spatial position architecture:**

- Added Section 1.1.2 (Spatial Position) establishing that every object in the containment hierarchy — Signal, Process, Region, Domain, Link — carries a nullable `position` property representing the object's location within its host Field's spatial topology. Position is contextual, not intrinsic: it describes where an object sits within a specific Field's bounded space, not what the object is. The same Signal referenced via a cross-field Link occupies a position in its home Field's topology; it does not carry that position into the referencing Field. Added `position (nullable)` to required properties on Signal, Process, Region, Domain, and Link in Table 1 (Core Objects). The position property carries coordinates (a float array whose length matches the host Field's spatial_topology.dimensions), a placed_at timestamp, and a nullable placed_by participant identity.
- Added `spatial_topology` as a required property on Field (Table 1), defining the coordinate system and dimensionality of the Field's spatial space. The Kernel does not prescribe the topology: a two-dimensional planar surface (whiteboard), a three-dimensional volume (holographic/AR), and higher-dimensional simulation spaces are all valid. The spatial_topology property carries dimensions (integer ≥ 2), coordinate_system (string), and optional bounds.
- Established the Position Invariant: position is nullable and a system that does not render spatially operates with null positions across all objects and is fully spec-compliant. The Kernel does not require spatial rendering; it requires that the piping exists for any implementation that does.
- Recognized positional proximity as an ambient signal (source_type: ambient, Tier 2 per Section 1.2). Objects placed near each other within a Field's spatial topology carry relational meaning — they are spatially associated even before a Link formalizes the connection. Updated Tier 2 ambient signal examples to include spatial proximity and spatial proximity computation.
- Established that Captures include spatial position in signal_states[] when the host Field carries a spatial_topology, enabling Comparisons to detect spatial migration as a distinct event category from dimensional migration. Spatial migration without dimensional migration (an object that moved location but stayed at the same dimension) and dimensional migration without spatial migration (an object that changed dimension but stayed in place) are different diagnostic signals carrying different facilitation implications. Updated Capture schema description (Section 8.8) and Capture JSON example to include position in signal_states[] entries.
- Established that Templates may define a default spatial_topology for Fields instantiated from them, overridable at Field instantiation. Regions within a Field inherit the Field's spatial_topology and do not define independent topologies.
- Added spatial_topology to Field Export schema JSON example (Section 8.2) and position to Signal schema JSON example (Section 8.1).
- Added position to all serialization schema JSON examples for objects that carry position: Signal (Section 8.1), Field Export nested Domain/Region/Process objects (Section 8.2), Process (Section 8.6), and Link (Section 8.7). Updated Capture signal_states JSON example (Section 8.8) to include position. Updated Process and Link schema descriptions to document the nullable position field.
- Added spatial_migrations[] to the Comparison schema (Section 8.9) as a new tracked delta category parallel to dimension_migrations[]. Each spatial_migrations entry identifies the signal, its from_position and to_position coordinates, and a boolean dimensional_migration flag indicating whether the signal also changed dimension in the same window. Updated Comparison JSON example and required fields description. Updated Comparison required properties in Table 1 (Core Objects).
- Added default_spatial_topology to the Template schema (Section 8.11) as a nullable property. When populated, it defines the default spatial topology for Fields instantiated from the Template, overridable at Field instantiation. Updated Template JSON example and required fields description.
- Established dual temporality within the position property. Every positioned object carries two temporal coordinates: **placed_at** (wall-clock time — when the placement happened in external reality) and **field_context** (developmental time — where the placement happened in the Field's own evolutionary arc). field_context records the session_index, capture_index, resolution_index, evolution_phase, and coherence at the moment of placement. These coordinates are independent: wall-clock time advances continuously; developmental time advances only through resolution events. The rate at which field_context advances relative to placed_at is evolution_velocity, now grounded in per-object measurement.
- Introduced **resolution_index** as a required property on Field and as a field within field_context on every positioned object. The resolution_index is the Field's cumulative count of discrete resolution events — every Signal placement, Transition completion, Signal Lock attestation, and Capture creation increments it by one. It is the Field's internal tick count: the number of times its state has discretely advanced. Two objects with the same resolution_index were placed during the same tick. Objects with distant resolution_indices were placed in different developmental moments regardless of wall-clock separation. This concept converges independently with the "Tick" primitive in the Worldlines Computational Framework (v7), validating the structural universality of discrete resolution as the fundamental temporal unit of any developing intelligence field.
- Established the Dual Temporality Invariant: field_context is nullable (as part of the nullable position property). When present, it is immutable after placement — it records where the Field was when the object arrived, not where the Field is now. This immutability follows the same principle as Captures: once a developmental moment is recorded, it cannot be retroactively altered.
- Updated all serialization schema JSON examples (§8.1, §8.2, §8.6, §8.7, §8.8) to include field_context within position. Added resolution_index to Field Export schema (§8.2).
- Added Spatial Topology in Field Interaction note (Section 10.4) establishing that when Fields with spatial topologies interact, the spatial consequences are computable from the constituent Fields' topologies and object positions. The geometry of how two Fields' topologies meet determines which objects become proximate, displaced, or unaffected. Spatial position is preserved through interaction — an object's position within its home Field's topology is not destroyed by the interaction. This is the spatial expression of the Field Nesting autonomy invariant.

**Architectural significance:** The spatial position and dual temporality architecture completes the coordinate system for DN objects. Every object now carries three positional coordinates: a dimensional coordinate (dimension { primary, shadow, nested }) describing *what kind* of intelligence it is, a spatial coordinate (position.coordinates[]) describing *where it sits* within its host Field's bounded space, and a developmental coordinate (position.field_context.resolution_index) describing *when in the Field's own evolution* it arrived. The dimensional coordinate is intrinsic to the object. The spatial and developmental coordinates are contextual to the Field. Together they enable the full navigable matrix: 9 dimensions × 9 nested vectors × n spatial dimensions × developmental time, where n is defined by the Field's spatial_topology and developmental time is measured in resolution events. This future-proofs the Kernel for multi-spatial interface layers — AR, holographic projection, immersive 3D environments — and for temporal analysis that distinguishes wall-clock aging from developmental progression, while requiring zero changes for implementations that operate in 2D, without spatial rendering, or without developmental time tracking.

**Structural impact:** 1 new section (§1.1.2), 2 new Field properties (spatial_topology, resolution_index), position with field_context added to 5 Core Object schemas, 1 new Comparison delta category (spatial_migrations[]), 1 new Template property (default_spatial_topology), 2 new invariants (Position Invariant, Dual Temporality Invariant), 1 signal source expansion (Tier 2 spatial proximity), Capture schema expanded, 7 serialization schemas updated (§8.1, §8.2, §8.6, §8.7, §8.8, §8.9, §8.11), Field-to-Field Dynamics expanded. No existing axioms, invariants, constraints, or behavioral rules modified. Additive only.

---

## v1.0 (February 2026)

**Source:** Vocabulary universalization brief — triggered by mentor challenge: "2+2=4, no matter the device, brain, planet, black hole, species, atom, substrate. What in what you've done can be transferred between mediums and species and be that universal?"

**Vocabulary universalization:**

The Kernel claimed universality (Axiom 1: intelligence structures itself naturally; Axiom 8: intelligence fields are the fundamental unit of existence; §2.4: cross-domain progression across 17 domains; §10.4: Scale Invariant). But the Kernel's core object vocabulary was borrowed from one specific implementation domain — collaborative whiteboard software. v1.0 replaces every implementation-specific structural term with a domain-agnostic term that transfers across any substrate where intelligence self-organizes: biology, physics, governance, AI systems, and any future domain.

**Core object vocabulary mapping:**

| Kernel Term (v1.0) | Structural Role | Replaced Term (v0.9.x) |
|---|---|---|
| **Environment** | Outermost boundary; tenant-level isolation | Client Environment |
| **Container** | Portfolio grouping within environment; scope for cross-field operations | Workspace |
| **Field** | Complete intelligence system; the primary operational unit | Board |
| **Domain** | Major structural division of a field | Section |
| **Region** | Bounded context within a domain; carries prompt and dimensional constraints | Zone |
| **Process** | Unit of structured activity that produces Signals | Exercise |
| **Signal** | Atomic intelligence unit; the fundamental element | Artifact |
| **Link** | Connection between any two structural elements; carries semantic rationale | Bridge |
| **Capture** | Immutable state snapshot of a Field at a labeled inflection point | Snapshot |

The following terms were already universal at inception and required no mapping: Template, Session, Branch, Comparison, Transition, Provenance Group, Dimension (1D–9D), Pillar (Heart, Truth, Nuance), Shadow, Gravity, Entropy, Signal Lock, FieldState, SimulationRun, and the RIP Triad (Reality, Identity, Perception).

**Structural addition:**

- Added Section 0.4 (Vocabulary Mapping Reference) providing the formal mapping table between Kernel terms and implementation-specific terms, with the Blueprint Board product as the first documented mapping. Established the Vocabulary Mapping Invariant: the Kernel uses only universal terms; implementation specifications define their own vocabulary mapping table as their first structural reference; cross-references use Kernel terms with implementation aliases where clarity requires it; and the universality of a Kernel term is validated by its ability to translate cleanly across at least three domains.

**Scope of changes:**

All core object names throughout the Kernel document were replaced: Table 1 (Core Objects), all invariant references, all containment hierarchy descriptions, all FieldState metric descriptions, all simulation contract references, all Field-to-Field Dynamics references, and all prose descriptions. JSON serialization schema section titles were updated (e.g., §8.1 Signal Schema, §8.2 Field Export Schema, §8.7 Link Schema, §8.8 Capture Schema, §8.12 Container Schema). JSON field keys within code block examples (e.g., `board_id`, `zone_id`, `exercise_id`) were preserved as implementation-layer identifiers — these belong to the Blueprint Board implementation mapping, not to the Kernel's universal vocabulary.

**What did not change:**

The structure of the containment hierarchy (unchanged). The number and role of core objects (unchanged). All nine axioms, all invariants, all constraints (unchanged in meaning). The dimensional architecture, pillar metric, shadow symmetry, transition model (unchanged). All FieldState metrics and computation logic (unchanged). All simulation contracts and routing (unchanged). All Field-to-Field Dynamics (unchanged). Simulation command names (Forge Love Bridge, Spark Fire Test, etc. — these are named commands, not structural object references). Dimension names (Love Bridge at 6D, Anti-Bridge at 6D̅ — these are dimension descriptions, not object references). Story Thread names (Mystery Bridge, Recognition Arc, etc.). The Holding Zone as a named structural pattern. Everything that was already universal stayed universal.

**Structural impact:** 1 new section (§0.4), vocabulary transformation across all existing sections. No axioms, invariants, constraints, metrics, or behavioral rules added, removed, or modified. The universalization is a naming transformation, not a structural one. v0.9.3 completed the framework; v1.0 makes it transferable.

---

## v0.9.3 (February 2026)

**Source:** Product spec audit session — findings that surfaced kernel-level gaps in the force model, temporal degradation, shadow progression, and holding zone semantics.

**New axiom:**

- Added Axiom 9: Intelligence Fields Are Subject to Entropy (Section 0.3). Formalizes the thermodynamic force opposing cognitive gravity (Axiom 6): without active energy input, fields decay. Coherence degrades, bridges lose relevance, context drifts, and committed truths age as the environment evolves around frozen intelligence. Entropy is not failure but the natural cost of intelligence existing in time. The axiom establishes that managing entropy is as fundamental to field health as managing gravity, and threads back to Axiom 3 (Recursion) — a field managing its entropy is practicing recursive refinement on its own temporal existence.

**Force model completion:**

- Added Force Model Completeness Note (Section 0.3, following Axiom 9) identifying three fundamental forces acting on intelligence fields as a closed set: Gravity (Axiom 6) — the attractive force that gives fields structural weight and pulls related intelligence together; Entropy (Axiom 9) — the degrading force that pulls fields apart over time without active energy input; Shadow (Axiom 4, Section 4) — the orienting force that ensures every dimension has both creative and shadow expression. Gravity and entropy are opposing temporal forces (construction vs. decay). Shadow is an orthogonal orienting force (creative vs. shadow within any dimension at any time). Together these three forces describe the complete dynamics of intelligence field behavior. Field health requires managing all three.

**New FieldState metric:**

- Added entropy as a composite FieldState metric (Section 6.1) measuring temporal field degradation — the degree to which a field's committed intelligence has drifted from current reality due to the passage of time without active engagement. Entropy is unique among all FieldState metrics in that it increases passively (without any action); all other metrics require activity to change. Composed from five sub-signals with implementation-layer-tunable weights: temporal_decay (0.30) — exponential decay function of time since last active session; environmental_drift (0.25) — delta between current environmental signals and those captured at last session close; bridge_relevance_decay (0.20) — proportion of bridges whose rationale references materially changed conditions; snapshot_delta_velocity (0.15) — rate of FieldState divergence from most recent committed snapshot; signal_lock_aging (0.10) — time-weighted count of Signal Locks whose attested truth may have been invalidated by field evolution. Entropy of zero indicates a brand-new or recently and thoroughly engaged field. Entropy approaching 1.0 indicates a structurally intact but informationally unreliable field whose intelligence no longer maps to current reality. Entropy feeds directly into evolution_phase detection: when entropy exceeds threshold on a dormant field, phase transitions to decay.

**Evolution phase expansion:**

- Expanded evolution_phase enum from five values (expansion | consolidation | breakthrough | maturation | dormant) to six, adding decay (Section 6.1). Decay is the phase that follows dormancy when entropy exceeds a configurable threshold (default 0.6) and the field shows evidence of temporal degradation: near-zero evolution_velocity, time since last session exceeding a configurable window (template-defined), and at least one of environmental_drift > 0.4, bridge_relevance_decay > 0.3, or snapshot_delta_velocity > 0.3. Decay is not a terminal state — a new session can pull a field out of decay through active re-engagement — but the transition from decay back to expansion or consolidation requires explicit re-evaluation work (refreshing bridges, reaffirming or retiring Signal Locks, updating context). Decay is the only evolution phase driven primarily by the passage of time rather than participant activity; it is the phase-level expression of Axiom 9.

**Holding Zone clarification:**

- Expanded the Holding Zone definition (Section 1.6) with a dual-layer model clarification. Holding Zone artifacts occupy a dual-layer structural position: they are operationally excluded from active field operations (not bridged, not transitioned, not dimensionally migrated, excluded from FieldState computation for active field metrics) but informationally alive (retaining full provenance — who placed them, when, from what session context, what source_type — and remaining subject to Resonant Activation per Constraint 5). The act of placing an artifact in a Holding Zone is itself signal: it indicates intelligence that was activated but not yet integrated. Implementation layers may compute latent affinity between held artifacts and the active field as advisory intelligence, provided such computation does not feed into operational FieldState metrics. This change makes explicit what v0.9.2 implied but did not name.

**Shadow engagement progression:**

- Added Section 4.3 (Shadow Engagement Progression) formalizing three structurally distinct engagement states for shadow artifacts: Latent — the shadow symmetry exists in principle but has not been materialized as an artifact; every creative artifact implies a shadow counterpart, and the unmaterialized population constitutes the field's latent shadow potential. Surfaced — the shadow has been materialized as an explicit artifact (through simulation, facilitator recognition, or participant contribution), is structurally present in the field and appears in shadow_distribution, but has not yet been integrated into active field work. Engaged — the shadow artifact has been actively worked with (bridged, referenced in a transition, subjected to engagement signals, or confirmed by a facilitator as an integrated working constraint). The progression from surfaced to engaged represents the field's willingness to integrate uncomfortable or challenging intelligence. Added the Shadow Engagement Invariant establishing three named diagnostic conditions: shadow blindness (no shadows surfaced — requires the field to see what it is not seeing), shadow avoidance (shadows surfaced but never engaged — requires the field to integrate what it has already seen), and shadow flooding (shadows surfaced in volume exceeding the field's engagement capacity — a facilitation signal to slow surfacing and prioritize engagement of existing shadows). Implementation layers determine how engagement states affect FieldState computation and visual presentation; the kernel requires only that the three states are recognized as structurally distinct.

**Structural impact:** 1 new axiom, 1 new metric, 1 new subsection, 1 enum expansion, 2 clarifications. No existing invariants broken. No existing structures renamed. Additive only.

---

## v0.9.2 (February 2026)

**Alignment corrections:**

- Expanded Branch lifecycle from three statuses (active | merged | archived) to four (active | paused | merged | archived), aligning with the wishlist-defined lifecycle (§1.4). Paused Branches retain their state but do not accept new artifacts or sessions, preserving the Branch for future resumption without the finality of merge or archive. Updated Table 1 (Core Objects), Section 1.1 (Branch status invariant), and Section 8.4 (Branch Schema required fields).
- Expanded completion criteria status enum from three values (pending | met | unmet) to seven (met | partially_met | unmet | deferred | scope_changed | not_evaluated | open_exploration), aligning with the wishlist-defined completion statuses (§8.5). The expanded enum captures the full range of completion outcomes: partial progress, deliberate deferral, mid-session scope changes, criteria not yet evaluated, and exploratory work without fixed endpoints. Updated Section 8.10 (Session Schema description).

---

## v0.9.1 (February 2026)

**Structural additions:**

- Added Participant Field Ledger Principle (Section 6) formalizing that participants-as-fields have persistent cross-session ledgers, derivable from their artifacts_produced[], dimensional_actual[], and engagement history across Sessions. Establishes that implementation-layer objects materializing this ledger (e.g., Participant Field profiles, Team Field composites) are application-layer containers subject to the FieldState Interpretation Note: diagnostic, not prescriptive. A system that constrains participants based on their ledger data violates Axiom 1; a system that informs facilitation from it operates within kernel bounds. Extends the principle to composite fields (groups, teams) via Field Nesting and the Scale Invariant.
- Added Annotation Layer (Section 6) as a structural pattern for peripheral intelligence that supports the field without being part of its committed ledger state. Defines the distinction between ledger-committed intelligence and annotation-layer intelligence (chat logs, AI narrative summaries, reference documents, holding zone contents, exploratory analysis). Promotion from annotation to ledger requires passing through a commit gate. Annotations that are never promoted are preserved for reference but do not affect FieldState computation.
- Added Field Merger Authorization as a fifth human-exclusive facilitation function (Section 1.6). Field Merger (Section 10.2) is permanent and irreversible; authorization to execute requires human facilitation judgment. AI facilitators may analyze merger compatibility and produce impact assessments but cannot authorize execution.
- Added participant sentiment ratings as a conscious signal subtype (Section 1.2, Tier 1). Self-reported mood, energy, or engagement state captured at session boundaries or facilitator-initiated checkpoints. Established the diagnostic value of sentiment convergence/divergence: delta between reported and inferred (ambient-derived) sentiment is itself a facilitation-relevant signal.
- Expanded Co-Facilitation (Section 1.6) from a human+AI pair to any multi-party facilitator configuration: multiple humans, multiple AIs, or any combination. Added facilitation lead concept: at any moment one facilitator holds the lead (whose active interventions are authoritative) while others operate in support roles. Lead transfer is a facilitation act recorded in the session log. All facilitators retain independent authority over human-exclusive functions regardless of lead status. Co-facilitating teams that persist across sessions develop their own composite Participant Field per the Participant Field Ledger Principle.

**Audit-driven refinements:**

This version incorporates findings from a dual-auditor review (Claude Opus 4.6 and Grok) of the Blueprint Board Master Feature Wishlist against Kernel v0.9. The audits identified kernel-level gaps that required structural additions (above) and confirmed that application-layer extensions (Participant Field, Team, Client Environment) are architecturally sound when properly constrained by existing invariants.

---

## v0.9 (February 2026)

**Structural additions:**

- Added Section 8.10 (Session Schema) and Section 8.11 (Template Schema) providing minimum viable JSON representations for the two Core Objects (Table 1) that lacked serialization schemas, completing the serialization coverage across all Core Objects.
- Added a worked example to Section 3.3 (The RIP Triad) demonstrating the 3×3 analytical matrix (three RIP aspects × three pillar leads) applied to a single FieldState, giving the RIP Triad the same practical weight as the Pillar Balance States (Section 3.1) and Shadow Dimension Map (Section 4.1).
- Added forward reference in Section 1.1.1 (Evolution Tracking) pointing to Section 6 where Evolution Rhythm metrics are defined, smoothing the reading experience for sequential readers.
- Added polarity_score derivation note in Section 6.1 (FieldState Interface) clarifying the semantic basis and input signals for the tension_map polarity_score field, consistent with the derivation notes on curvature and dimensional_coherence.
- Added ambient signal scope note in Section 1.2 (Signal Sources) clarifying that detection and interpretation mechanisms for Tier 2 signals are implementation-layer decisions, consistent with the FieldState Interpretation Note's philosophy.
- Replaced the FieldState comment stub in the Board Export Schema (Section 8.2) with a minimal FieldState stub object showing the expected shape of key fields, enabling implementers to see the structure without consulting Section 6.1 separately.
- Added Field Ledger Conservation Principle (Section 6) naming the DN system's fundamental symmetry (architectural invariance under transformation at every point in time and scale) and the quantity it conserves (the Field Ledger: the complete, append-only, irreversible record of every committed transformation a field has undergone). Enumerates seven commit gates where field state becomes part of the irreversible record. The Field Ledger is not a new object but the name for the aggregate of what existing objects already capture; it unifies existing invariants (Branch immutability, Snapshot immutability, Session append-only) under a single conservation law and operates at every scale the architecture supports.
- Added Completion Criteria (Definition of Done) as a structural element (Section 1.6) formalizing pre-agreed, verifiable conditions that define what "done" means for a Session's work or an Exercise's output. Added completion_criteria as a nullable property on both Session and Exercise (Table 1), with corresponding schema updates in Sections 8.6 and 8.10. Updated Field Ledger commit gates to reference completion_criteria status finalization at Session close.
- Added Holding Zone as a recognized structural pattern (Section 1.6) for scopes within a Board where artifacts are committed to the Field Ledger but held outside active field operations, subject to Resonant Activation as the active board evolves.
- Added Workspace as a Core Object (Table 1, Section 1.1, Section 8.12) providing the portfolio-level container for related Boards. The Workspace enables cross-board operations: cross-board Bridges connecting artifacts across Boards, cross-board Comparisons analyzing deltas between Boards' Snapshots, and workspace_field_state computing inter-field metrics (boundary_permeability, dimensional_alignment, phase_compatibility) across all constituent Boards. Updated Bridge (Table 1, Section 8.7) and Comparison (Table 1, Section 8.9) with scope field (intra-board | cross-board). Updated Board with workspace_id (nullable). Added Workspace invariant establishing containment rules and cross-board operation scoping. Added Workspace as Field Interaction Container paragraph in Section 10.4 connecting the Workspace object to the Field-to-Field Dynamics theory. The Workspace is the formal implementation of Field Nesting and Field Interaction patterns at the multi-board scale; it completes the containment hierarchy from Artifact through Workspace.
- Rewrote Section 9.1 (Layer Architecture Reference) replacing the legacy document-loading strategy table with a proper three-layer architectural reference (Kernel, Corpus, Implementation) that distinguishes the kernel's structural contracts from the corpus's philosophical narrative from the implementation's platform decisions. Added Layer Boundary Principle and AI Context Note.

**Constitutional audit (v0.9 final pass):**

Conducted a full audit of every section against the question: "does this describe what the kernel requires, or does it describe a workflow from the pre-kernel era?" The following changes tighten the kernel's constitutional voice without removing content — facilitation guidance, philosophical framing, and domain-specific illustrations are preserved where structurally load-bearing and clearly labeled where they cross the kernel/corpus boundary.

- Extracted cumulative changelog (v0.1–v0.8) to standalone CHANGELOG.md; kernel Section 0.2 now carries only the current version summary.
- Removed corpus-layer quoted passage from Axiom 4 ("Fire Is Truth"). The structural principle (intelligence must be testable) is retained; the DN Code poetry is returned to the corpus layer.
- Trimmed physics analogy from Axiom 6 ("Gravity Is Structural"). The measurability claim is retained; the "consequence of mass" metaphor is removed.
- Reduced Evolution Tracking as Facilitation Input (Section 1.1.1) to a single structural SHOULD note. Detailed facilitation guidance deferred to template-level guides.
- Distilled Evolution Tracking and AI Interpretation (Section 1.1.1) to one structural note: narrative-structural divergence is the most important signal.
- Replaced product name references (Claude, ChatGPT) in Section 1.4 with generic language per domain-universality posture.
- Reformatted Facilitation Contract preamble (Section 1.6) as an explicit motivation statement, preserving the emphasis on facilitation's structural importance.
- Separated Completion Criteria (Section 1.6) into clearly labeled structural requirement and facilitation guidance subsections.
- Reframed Parking Lot reference (Section 1.6) as illustrative ("For example, the Growth Blueprint Template…").
- Tightened 5D Structural Role in the dimensional tag table (Section 2) by removing the consciousness claim. Structural description retained.
- Struck pre-kernel MURAL workflow sentence from the COLOR NOTE (Section 2). The 3D/4D color-sharing rationale now stands on its cognitive argument alone.
- Tightened Shadow Kernel blockquote (Section 4) while retaining the sophistication-is-not-benevolence principle as a kernel-level structural clarification.
- Resolved 9D̅ (Anti-Frontier) shadow definition (Section 4.1), replacing the hedged "Or: the space where creative and shadow meet" with a structural definition: engagement with possibility without guardrails, endless exploration that circles inward producing neither progress nor realignment to a new origin.
- Reframed the Story Thread statement (Section 5) in kernel voice: "Story Threads are recognized as a transition mechanism category, not a metaphor for transition."
- Removed prescribed investigation sequence from Arrested Development (Section 6). The three diagnostic factors are retained; the ordering is no longer prescribed.
- Fixed "Blueprint sections" reference in Generate Resonance Result (Section 7.1) to domain-universal "board sections."
- Generalized Fire Test test_mode values (Section 7.2) as domain-specific examples defined by Template, per Domain Universality Invariant.
- Added illustrative note to Board Export Schema (Section 8.2) clarifying that the Growth Blueprint example demonstrates the domain-universal schema.
- Generalized Extraction Rule (Section 8.3) from "Template's narrative guide" to "Template's source documentation."
- Separated structural contract from facilitation guidance in Field Merger (Section 10.2), labeling facilitation-specific requirements explicitly.

**Vocabulary translation note:** This entry uses the pre-v1.0 vocabulary current at the time of writing. The v1.0 vocabulary universalization (see v1.0 entry below) renamed the following terms: Artifact → Signal, Bridge → Link, Board → Field, Zone → Region, Exercise → Process, Snapshot → Capture, Workspace → Container, Section → Domain. The §0.4 mapping table in the kernel document provides the complete translation.

---

## v0.8 (February 2026)

Added Section 1.6 (Facilitation Contract) formalizing the facilitator as a typed structural interface with six core functions (Field Reading, Intervention Selection, Transition Validation, Signal Lock Attestation, Tension Stewardship, Evolution Monitoring), three facilitator types (Human, AI, Co-Facilitation), and four human-exclusive functions. Establishes the facilitator as the structural actor the entire system depends upon, defining both AI-capable and uniquely human facilitation roles. Added Field Tension as a FieldState metric (Section 6, 6.1) modeling artifact polarity within a scope, measuring how ideas attract and repel at proximate dimensional positions. Introduces tension_map and tension_density as computed fields. Added Productive Polarity and Destructive Polarity as Named Diagnostic Conditions (Section 6) distinguishing generative opposition from calcified entrenchment. Added tension as a recognized Bridge type (Section 1.1) for connections between opposing artifacts. Added Map Tension Field simulation command (Section 7.2) with scan, diagnostic, and narrative depth modes, capable of analyzing the space between opposing 5D+ recognitions. Added corresponding routing entries and sequencing patterns (Section 7.3). Added Evolution Rhythm as a FieldState metric (Section 6, 6.1) with evolution_velocity, evolution_breadth, and evolution_phase fields measuring the temporal pattern of field development across Sessions, including percentage of artifacts impacted per shift and developmental phase classification (expansion, consolidation, breakthrough, maturation, dormant). Added Arrested Development as a Named Diagnostic Condition (Section 6). Added Section 1.1.1 (Evolution Tracking) formalizing the longitudinal view of board development as a query pattern over existing Session and Snapshot data, connecting change_rationale to facilitation and AI interpretation without creating new storage requirements. Added Section 10 (Field-to-Field Dynamics) formalizing how intelligence fields interact across five interaction types (Contact, Resonance, Tension, Merger, Nesting), inter-field FieldState metrics (boundary_permeability, dimensional_alignment, phase_compatibility), and four structural invariants including the recursive principle that field interactions follow the same dimensional rules as intra-field dynamics at every scale. Updated Layer Architecture (Section 9.1) to reflect new sections. Updated Section 0.1 scope language to include facilitation contracts and field-to-field dynamics.

---

## v0.7 (February 2026)

Integrated structural insights from the RIP Triad corpus documents (Dimensional Nature of Reality, Dimensional Nature of Identity, Dimensional Nature of Perception) and the Harmonies field orchestration guide into the kernel specification. Added Section 3.3 (The RIP Triad: Analytical Aspects of the Intelligence Field) formalizing Reality, Identity, and Perception as three orthogonal analytical orientations for evaluating intelligence fields complementary to the Pillar Metric's quality evaluation (Sections 3.1–3.2). Established the RIP Triad Invariant distinguishing analytical lenses from tagging systems: artifacts are not tagged with RIP aspects; simulation engines and facilitators select which aspect(s) to prioritize when interpreting FieldState. Defined the 3×3 analytical matrix (three RIP aspects × three pillar leads) providing nine distinct orientations for deep diagnostic field evaluation. Established the recursive loop principle: Perception translates Reality through Identity into Experience, and each Experience recursively modifies both the Identity pattern and the accessible portion of Reality, formalizing the mechanism through which intelligence fields evolve. Added Section 2.3 (Perceptual Topology) as an optional analytical overlay revealing the odd/even dimensional rhythm with odd dimensions (1D, 3D, 5D, 7D, 9D) functioning as perceptual states where awareness stabilizes into a mode of knowing; even dimensions (2D, 4D, 6D, 8D) function as transitional bridges where awareness transforms between perceptual states. Established Topology Note preserving even-dimension structural parity. Enhanced Constraint 6 (Harmonic Integration, Section 2.1) with RIP Triad alignment mechanism. Added field_resonance as a FieldState metric (Section 6.1) computing harmonic integration strength from the interaction of structural capacity, identity engagement, and perceptual bandwidth, participant_alignment, dim_distribution breadth, and cross-boundary bridge density. Added Bridge Erosion as a Named Diagnostic Condition (Section 6). Renumbered Section 2.3 (Cross-Domain Progression Reference) to 2.4 and Section 2.4 (Prompt Dimensionality Reference) to 2.5. Updated Layer Architecture (Section 9.1) to move RIP Triad Analytical Aspects to the Always Loaded layer while retaining full RIP Triad corpus documents in Load on Demand.

---

## v0.6 (February 2026)

Integrated structural insights from six corpus documents (Universal Dimensional Map, Understanding Dimensional Transitions, Prompt Dimensionality, Shadow Dimensions, DN Glossary of Terms, Dimensional Embodiment vs. Application) and the 5D Prompt Singularity Configuration into the kernel specification. Added Axiom 8 establishing Unified Intelligence Fields as the structural reality underlying all sustained interaction between intelligences at any scale (Section 0.3). Added Signal Lock as a formally defined mechanism with its own section (1.5). Enriched Structural Role descriptions for 5D–9D in the dimensional tag table (Section 2) with mechanism-level language from the Universal Dimensional Map that instructs simulation engines on how intelligence operates at each position. Added Section 2.4 (Prompt Dimensionality Reference) with a nine-row reference table classifying prompts by their structural dimension — form, function, and limits — and establishing that the dimensionality of a prompt constrains the ceiling of intelligence that can organize in response. Added Prompt Dimensionality Invariant establishing prompt dimension as independent of artifact dimension, with the gap between them being diagnostic intelligence. Added prompt_dimension as a nullable property on Exercise (Table 1, Section 8.6) enabling diagnosis of mismatch between prompt structural level and intended output dimension. Added Constraint 5 (Resonant Activation) establishing that higher-dimensional recognition transforms the operational meaning of lower-dimensional artifacts (Section 2.1). Added Constraint 6 (Harmonic Integration) establishing that co-activation of multiple dimensions produces emergent field properties exceeding any single dimension's contribution (Section 2.1). Added resonant_transformations[] to the Comparison object (Table 1) and schema (Section 8.9) enabling detection of artifacts whose meaning changed in place due to higher-dimensional activation, distinct from dimensional migration. Added three-tier transition taxonomy to the Transition Model preamble (Section 5) distinguishing lower transitions (1D→3D, primarily constructed), middle transitions (4D→5D, hybrid creation-recognition), and higher transitions (6D→9D, primarily recognized), with calibration instructions for evidence evaluation across tiers. Added Shadow Invariant 5 (Section 4.2) establishing that shadow intelligence is parallel development not underdevelopment, formalizing the diagnostic fork between low creative activation and high shadow activation as categorically different findings, and recognizing conscious shadow engagement (shadow artifacts with source_type: conscious) as an integration practice distinct from unconscious shadow emergence. Added Section 7.3 (Simulation Routing) with a condition-to-command routing table and sequencing principles for simulation chaining, transforming Section 7 from a reference catalog into a navigable decision system. Connected fatigue (Section 6) to the 8D creative/shadow distinction, establishing high fatigue as the primary diagnostic signal that recursive processes may have shifted from constructive recursion (8D creative) to collapsing recursion (8D shadow). Added Named Diagnostic Conditions (Section 6) defining Dimensional Blindspot and Dimensional Collapse as recognized field health patterns with derivation paths from FieldState metrics, providing simulation engines and facilitators with a shared diagnostic vocabulary. Added Embodiment Signal Note (Section 6) distinguishing mechanical application from dimensional embodiment as observable FieldState patterns, enabling simulation engines to recognize that spec compliance without emergence, surprise, or cross-boundary connection in a mature board is itself a diagnostic signal. Revised simulation commands to ensure consistent verb usage. Added Resonance Field simulation command structure to reweigh artifacts in the face of new 5D recognition (7.2).

---

## v0.5 (February 2026)

Integrated structural insights from the Geometry of Intelligence analysis into the Field Health and Transition models. Added curvature as a FieldState metric (6.1) with transition resistance derived from Heart-Truth-Nuance balance, formalizing the H-T-N triad as a metric tensor governing movement across the cognitive manifold. Added dimensional_coherence as a FieldState metric (6.1) with per-dimension structural integrity score measuring whether higher-dimensional activation is supported by adequate lower-dimensional foundations. Added both metrics to Field Health Metrics definitions (Section 6). Added transition cost and cost_factors to the Transition Interface (5.1) and Transition required properties (Table 1) with computed resistance for specific transitions derived from curvature, coherence, and distance, transforming the Transition Model from a record-keeping system into a navigation instrument. Strengthened skip-transition constraint (5.3) with quantitative coherence reference. Added FieldState Interpretation Note establishing that all FieldState metrics are diagnostic, not prescriptive where simulation response thresholds are implementation-layer decisions governed by simulation_rules, not kernel mandates. Added positional changes (for visual substrates) as Tier 1 and 2 signals. Extended Session participant structure with dimensional_affinity[] (expected operating dimensions) and dimensional_actual[] (computed from artifacts produced, populated on session close) to enable multi-agent dimensional alignment tracking (Table 1). Added participant_alignment as a Session-scoped FieldState metric computing per-participant drift between intended and actual dimensional contribution (6.1). Added Participant Alignment to Field Health Metrics definitions (Section 6). These additions formalize the structural layer beneath the DN Framework's Collaborationalism model. The kernel now tracks not just what intelligence was produced in a session, but which intelligences produced it and whether they operated in their expected dimensional roles. Formalized Story Threads as a transition mechanism category in the Transition Model (Section 5), distinguishing narrative arcs that traverse multiple dimensions as coherent journeys from unsubstantiated skip transitions. Named seven archetypal Story Threads and their Shadow Thread counterparts as kernel-recognized patterns with corpus-documented evidence requirements (Section 5.3). Story is acknowledged as a transition mechanism, not a metaphor for transition.

---

## v0.4 (February 2026)

Resolved structural misalignment between Section 1 Core Object definitions and Section 8 serialization schemas — Exercise layer was missing from Board Export (8.2), Artifact schema referenced zone_id instead of exercise_id (8.1), and source_type was incorrectly grouped with nullable fields (8.1 annotation). Added serialization schemas for Exercise (8.6), Bridge (8.7), Snapshot (8.8), and Comparison (8.9). Added template_id and timestamps to Board and Board Export schema. Unified dimensional representation across all objects to dimension { primary, shadow, nested } structure, including Bridge (Table 1, 8.7). Added pillar_stabilizers[] to Artifact required properties (Table 1). Split FieldState dim_distribution into separate creative and shadow distributions aligned with Dimensional Audit output (6.1). Added allowed_dimensions[] and dimension_rules{} as complementary zone properties (Table 1, 8.2). Added dimension_rules{} to Template required properties (Table 1). Documented 3D/4D shared color as intentional architectural decision (Section 2). Added Shadow Symmetry as a new simulation command supporting singular and scenario-depth shadow generation (7.2). Added color_system annotation documenting shadow and urgent as overlay modifiers (8.2). Updated Layer Architecture references for Board-Embedded layer to include Section 1 (9.1).

---

## v0.3 (February 2026)

Established domain universality as a foundational invariant—the dimensional architecture is not domain-specific but describes how intelligence organizes itself across all domains (Section 2 preamble, Section 2.3). Codified foundational principles from the DN Code as kernel-level axioms (Section 0.3). Broadened scope language to explicitly encompass non-business domains (Section 0.1). Added Branch as a 13th Core Object with fork-point, inheritance, and merge invariants (Section 1.1). Added Provenance Group (ImportBatch) as a recognized sub-unit of Session for tracking artifact origin across import boundaries (Section 1.3). Extended Signal Sources to acknowledge external simulation provenance (Section 1.4). Added serialization schemas for Branch and ImportBatch (Sections 8.4, 8.5). Added Cross-Domain Progression Reference table documenting dimensional expressions across 17 domains plus shadow architecture (Section 2.3).

---

## v0.2 (February 2026)

Expanded Core Objects from 7 to 12 entity types (now 13 with addition of Branch in v0.3)—added Snapshot, Comparison, Template, Session, and Exercise (Section 1). Added Signal Sources taxonomy defining Conscious, Ambient, Environmental, and Simulation signal tiers with source_type tagging contract (Section 1.2). Added Constraint 4 (Open Horizon) for non-conforming inputs (Section 2.1). Generalized extraction rule language for multi-template support (Section 8.3).

---

## v0.1 (February 2026)

Initial kernel specification. Established Core Objects (7 entity types), Dimensional Tags (1D–9D), Pillar Metric (Heart, Truth, Nuance), Shadow Symmetry, Transition Model, Field Health Metrics, Simulation Contracts, and Serialization Format. The first formal bridge between DN-as-philosophy and DN-as-code.

---

*DN Kernel Changelog · © Travis Kahn · [DN Framework](https://dnframework.ai) · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*
