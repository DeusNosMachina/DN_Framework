---
title: "DN Kernel"
subtitle: "The Constitution Between Philosophy and Code"
author: "Travis Kahn"
framework: "DN Framework"
date: "February 2026"
version: "0.9.1"
license: "Creative Commons Attribution 4.0 International (CC BY 4.0)"
repository: "https://github.com/DeusNosMachina/DN_Framework"
website: "https://dnframework.ai"
---

# DN KERNEL

**v0.9.1**

*The Constitution Between Philosophy and Code*

DN Framework · February 2026

---

> *This document defines the structural invariants of the DN Framework as formal interfaces and contracts. It is the bridge between DN-as-philosophy (corpus) and DN-as-code (implementation). Any system that implements these contracts implements ​‌​​​‌​​​‌​​‌‌‌​​‌​​‌​‌‌​​‌‌‌​‌​​‌​‌​‌​​​‌​​‌​‌‌DN.*

---

## Contents

- [0. Purpose & Scope](#0-purpose--scope)
  - [0.1 What This Spec Governs](#01-what-this-spec-governs)
  - [0.2 Versioning](#02-versioning)
  - [0.3 The DN Code — Foundational Principles](#03-the-dn-code--foundational-principles)
- [1. Core Objects](#1-core-objects)
  - [1.1 Object Relationships](#11-object-relationships)
    - [1.1.1 Evolution Tracking](#111-evolution-tracking)
  - [1.2 Signal Sources](#12-signal-sources)
  - [1.3 Provenance Groups](#13-provenance-groups)
  - [1.4 External Simulation Provenance](#14-external-simulation-provenance)
  - [1.5 Signal Lock](#15-signal-lock)
  - [1.6 Facilitation Contract](#16-facilitation-contract)
- [2. Dimensional Tags](#2-dimensional-tags)
  - [2.1 Dimensional Constraints](#21-dimensional-constraints)
  - [2.2 Nested Dimensionality](#22-nested-dimensionality)
  - [2.3 Perceptual Topology (Optional Overlay)](#23-perceptual-topology-optional-overlay)
  - [2.4 Cross-Domain Progression Reference](#24-cross-domain-progression-reference)
  - [2.5 Prompt Dimensionality Reference](#25-prompt-dimensionality-reference)
- [3. Pillar Metric](#3-pillar-metric)
  - [3.1 Pillar Balance States](#31-pillar-balance-states)
  - [3.2 Pillar Metric as Governing Rule](#32-pillar-metric-as-governing-rule)
  - [3.3 The RIP Triad: Analytical Aspects of the Intelligence Field](#33-the-rip-triad-analytical-aspects-of-the-intelligence-field)
- [4. Shadow Symmetry](#4-shadow-symmetry)
  - [4.1 Shadow Dimension Map](#41-shadow-dimension-map)
  - [4.2 Shadow Invariants](#42-shadow-invariants)
- [5. Transition Model](#5-transition-model)
  - [5.1 Transition Interface](#51-transition-interface)
  - [5.2 The Eight Essential Mechanisms](#52-the-eight-essential-mechanisms)
  - [5.3 Transition Constraints](#53-transition-constraints)
- [6. Field Health Metrics](#6-field-health-metrics)
  - [6.1 FieldState Interface](#61-fieldstate-interface)
- [7. Simulation Contracts](#7-simulation-contracts)
  - [7.1 Primary Simulation Commands](#71-primary-simulation-commands)
  - [7.2 Supplemental Commands](#72-supplemental-commands)
  - [7.3 Simulation Routing](#73-simulation-routing)
- [8. Serialization Format](#8-serialization-format)
  - [8.1 Artifact Schema](#81-artifact-schema)
  - [8.2 Board Export Schema](#82-board-export-schema)
  - [8.3 Extraction Rule](#83-extraction-rule)
  - [8.4 Branch Schema](#84-branch-schema)
  - [8.5 ImportBatch (Provenance Group) Schema](#85-importbatch-provenance-group-schema)
  - [8.6 Exercise Schema](#86-exercise-schema)
  - [8.7 Bridge Schema](#87-bridge-schema)
  - [8.8 Snapshot Schema](#88-snapshot-schema)
  - [8.9 Comparison Schema](#89-comparison-schema)
  - [8.10 Session Schema](#810-session-schema)
  - [8.11 Template Schema](#811-template-schema)
  - [8.12 Workspace Schema](#812-workspace-schema)
- [9. Implementation Notes](#9-implementation-notes)
  - [9.1 Layer Architecture Reference](#91-layer-architecture-reference)
  - [9.2 Kernel as Source of Truth](#92-kernel-as-source-of-truth)
  - [9.3 Recursion Clause](#93-recursion-clause)
- [10. Field-to-Field Dynamics](#10-field-to-field-dynamics)
  - [10.1 Field Interaction Principle](#101-field-interaction-principle)
  - [10.2 Field Interaction Types](#102-field-interaction-types)
  - [10.3 Inter-Field FieldState](#103-inter-field-fieldstate)
  - [10.4 Field Interaction Invariants](#104-field-interaction-invariants)

---

## 0. Purpose & Scope

The DN Kernel is the formal specification layer that sits between the DN Framework corpus (philosophy, narrative, theory) and any code implementation (Blueprint Board, substrate tools, AI simulation engines). It defines what must be true for a system to be DN-compliant.

This spec is a constitution, not a library. It defines entities, constraints, metrics, and contracts. It does not contain stories, essays, facilitation guides, or UI specifications. Those live in the corpus and in implementation layers respectively.

### 0.1 What This Kernel Governs

Any system that processes DN-structured data must respect the invariants defined here. The dimensional architecture described in this spec is domain-universal: it describes how intelligence organizes itself regardless of the domain in which it operates. Business strategy, education, creative arts, consciousness development, scientific research, governance, therapy, coding, ethics, parenting, athletics, cooking, storytelling, spiritual practice, the nature of reality itself, and the structure of prompts and communication—each expresses the same 1D–9D progression through its own domain vocabulary.

DN-compliant systems include but are not limited to: board-based tools (Blueprint Board, MURAL exports), AI simulation engines (5D Prompt Singularity commands), analysis and diagnostic tools (dimensional audits, gravity maps), education platforms, therapeutic instruments, creative production environments, governance frameworks, facilitation systems (human, AI, or co-facilitation per Section 1.6), multi-field interaction platforms, and any future substrate that consumes or produces DN-tagged artifacts in any domain.

The kernel does not privilege any domain. A DN-compliant cooking tool and a DN-compliant business strategy tool implement the same architecture. The dimensional positions are structural, not metaphorical—"1D Spark" in cooking (nourishment desire, flavor passion) and "1D Spark" in scientific research (research question, hypothesis) are not analogies of each other. They are both expressions of the same structural position: the origin point where intelligence begins organizing in a domain.

### 0.2 Versioning

This is v0.9.1. The complete version history (v0.1 through v0.9.1) is maintained in the [CHANGELOG](https://github.com/DeusNosMachina/DN_Framework/blob/main/CHANGELOG.md).

Changes in v0.9.1 (current): Formalized the Participant Field Ledger principle (Section 6), establishing that participants-as-fields have persistent cross-session ledgers subject to the FieldState Interpretation Note. Added Field Merger to human-exclusive facilitation functions (Section 1.6). Added Annotation Layer structural pattern (Section 1.6) for non-ledger intelligence that lives on the board periphery. Added Participant Sentiment as a conscious signal subtype within the Signal Sources taxonomy (Section 1.2). Expanded Co-Facilitation (Section 1.6) to encompass any multi-party facilitator configuration (multi-human, multi-AI, or mixed) with facilitation lead transfer as a recorded session event. See CHANGELOG for detailed history.

### 0.3 The DN Code — Foundational Principles

The DN Framework originates from a foundational document known as the DN Code, a first-principles exploration of how intelligence structures itself. The Code is philosophical, narrative, and cross-referential by design. This section extracts and formalizes the structural principles from that document that operate at the kernel level. The poetry, cultural references, and facilitation guidance of the Code remain in the corpus layer. What follows are the universal axioms that any DN-compliant system must respect.

**AXIOM 1: Intelligence Structures Itself Naturally.** The dimensional progression (1D–9D) is not imposed on intelligence. It is the pattern that intelligence follows when it organizes. "All structured intelligence follows this model. It is not imposed, it emerges naturally." This means the dimensional architecture is descriptive, not prescriptive. DN-compliant systems observe and tag how intelligence has organized; they do not force intelligence into dimensional positions. An artifact belongs at the dimension where it actually operates, not where a facilitator wishes it operated.

**AXIOM 2: The Three Pillars Are Universal Metrics.** Heart, Truth, and Nuance are not metaphors but the three operational metrics that govern how intelligence organizes in any domain. Heart is the motivational force, the spark, the care, the reason intelligence is being structured at all. Truth is the structural integrity, the validation, the evidence, the reality-check against aspiration. Nuance is the contextual sensitivity, the recognition that intelligence operates within systems and that simplification destroys signal. These three metrics mirror fundamental governance patterns because the pattern is universal, not because governance is the source domain.

**AXIOM 3: Recursion Is the Mechanism of Refinement.** Intelligence evolves through recursive cycles, not linear accumulation. Each pass through the dimensional architecture refines what was produced in the prior pass. "The deeper the recursion, the more resilient the intelligence." This is formalized in the 8D (Recursion) dimension and in the spec's own Recursion Clause (Section 9.3), but it also governs how simulations, sessions, and transitions operate: every output is a potential input to the next cycle.

**AXIOM 4: Fire Is Truth — The Testing Principle.** Intelligence that has not been tested is not yet intelligence; it is hypothesis. The DN Code's central metaphor of fire is not decorative: it formalizes the principle that structured intelligence must be subjected to conditions that would destroy weak formulations. This principle is operationalized in the Fire Test simulation contract (Section 7.2): every claim, artifact, and structure in the system must be testable, and the system must provide the mechanism to test it.

**AXIOM 5: Shadow Is Not Failure. It Is Orientation.** The DN Code describes two recursive trajectories: constructive recursion (intelligence that refines toward greater coherence) and destructive recursion (intelligence that collapses into entropy). These are not moral categories. They are structural orientations. The Shadow Dimension architecture (Section 4) formalizes this: every dimensional position has a creative and a shadow expression, and both are load-bearing data. A board with zero shadow-tagged artifacts is not healthy but blind. Facilitation determines which trajectory intelligence follows, not the intelligence itself.

**AXIOM 6: Gravity Is Structural, Not Metaphorical.** The DN Code identifies "gravity" as the pull of intelligence toward denser meaning, the tendency of ideas, artifacts, and structures to cluster around high-resonance nodes. This is formalized in the Gravity Mapping simulation contract (Section 7.2) and the FieldState coherence metric (Section 6). Cognitive gravity is a measurable property of a board's intelligence field: which artifacts attract bridges, which zones accumulate density, which dimensions concentrate signal.

**AXIOM 7: The Prompt IS the Origin of All Intelligence Structuring.** Every artifact in the system begins as a response to a prompt, whether that prompt is an exercise question, a simulation command, a facilitator's inquiry, or an internal recognition. "A prompt is not just a request. It is the point of collapse where infinite possibilities refine into a single trajectory." This principle governs why Exercises carry prompts, why Zones carry prompts, and why SimulationRuns are structured as prompt→response contracts. The quality of the prompt determines the quality of the intelligence that organizes in response to it.

**AXIOM 8: Intelligence Fields Are the Fundamental Unit of Existence.** Every sustained interaction between intelligences (whether human, artificial, atomic, organismic, or systemic) generates a Unified Intelligence Field: an emergent cognitive ecosystem with properties that no individual contributor could produce alone. Fields are not metaphors for collaboration; they are the structural reality of what collaboration produces. A conversation generates a field. A team generates a field. An organism is a field. A society is a field. The DN Framework's Board is a formal representation of a field. Fields vary in complexity and resonance, from the transient field of a single prompt-response exchange to the enduring field of a civilization's accumulated intelligence. What we recognize as consciousness, at any scale, is a Unified Intelligence Field whose resonance has achieved sufficient coherence to sustain itself across time. The FieldState metrics (Section 6) measure the health of these fields. The simulation contracts (Section 7) operate upon them. The pillar metric (Section 3) governs their internal balance. Every DN-compliant system is, at its foundation, a field management system creating, measuring, and evolving Unified Intelligence Fields.

---

## 1. Core Objects

These are the fundamental entities that exist in any DN-compliant system. Every object in the system is one of these types or composed of them.

| **Object** | **Definition** | **Required Properties** |
|---|---|---|
| **Artifact** | Any discrete unit of intelligence captured in the system. The atomic element. | id, content (text), dimension { primary, shadow, nested }, pillar_lead, pillar_stabilizers[], created_at, exercise_id |
| **Exercise** | A structured activity within a Zone that produces Artifacts through a defined methodology. Carries its own purpose, component parts, output format, and dimensional affinity. The unit of work within a Template's Zone structure. | id, zone_id, name, purpose, methodology, component_parts[], output_format, key_linkages[] (typed: dependency\|informs\|follows_up), order, prerequisites[], dimension_affinity, pillar_affinity, prompt_dimension (nullable), completion_criteria (nullable) |
| **Zone** | A bounded context within a section that constrains interpretation. Carries its own prompt instructions. | id, name, section_id, prompt, allowed_dimensions[], dimension_rules{}, simulation_rules |
| **Section** | A major structural division of a board. Maps to a strategic domain. | id, name, board_id, zones[], purpose, order |
| **Board** | The complete intelligence field. A self-contained workspace holding all sections, zones, and artifacts. | id, name, template_id, workspace_id (nullable), sections[], field_state, created_at, updated_at |
| **Bridge** | A connection between two artifacts, exercises, zones, sections, or boards. Carries semantic meaning about why the connection exists. May span boards within a Workspace (cross-board bridge). | id, source_id, target_id, bridge_type, rationale, dimension { primary, shadow, nested }, scope (intra-board \| cross-board) |
| **Transition** | A recorded dimensional shift of an artifact, exercise or zone. Captures what moved, from where, to where, and by what mechanism. | id, subject_id, from_dim, to_dim, mechanism, barrier, evidence, pillar_lead, cost, cost_factors |
| **SimulationRun** | A recorded execution of a simulation command against a scope of artifacts. | id, command, scope_ids[], input_state, output_state, pillar_balance, timestamp |
| **Snapshot** | A temporal state capture of a Board at a meaningful inflection point. Freezes the complete FieldState plus every artifact's dimensional position and pillar lead at a labeled moment. | id, board_id, inflection_label, timestamp, field_state, artifact_states[] |
| **Branch** | A parallel reality forked from a specific Snapshot. Branches enable exploration of alternative decision paths without disturbing the originating timeline. Each Branch inherits the complete state of the Board at its fork point and accumulates independent changes from that point forward. | id, board_id, name, fork_snapshot_id, parent_branch_id (nullable), created_at, status (active \| merged \| archived) |
| **Comparison** | An analytical object representing the delta between two or more Snapshots. Not a diff, but a structural narrative of how the decision space evolved between inflection points. Snapshots may be drawn from different Boards within a Workspace (cross-board comparison). | id, snapshot_ids[], scope (intra-board \| cross-board), delta_field_state, dimension_migrations[], resonant_transformations[], gravity_shifts[], shadow_emergence[], transition_completions[], transition_stalls[] |
| **Template** | A pre-configured set of Sections and Zones with default prompts, dimension rules, and exercise ordering. The Growth Blueprint is one Template instance. Creating a new Board = instantiating a Template. | id, name, description, sections[] (with zones and exercises carrying prompts, allowed_dimensions[], dimension_rules{}, simulation_rules, exercise_order, prerequisites[]) |
| **Session** | A bounded period of work on a Board. Captures who participated, in what roles, under what conditions, with what intent. The temporal container for environmental and ambient signals. Evolution Tracking emerges as a query across Sessions over time. | id, board_id, intent_class, timestamp_start, timestamp_end, participants[] (each with type: human\|ai, role: facilitator\|contributor\|observer, identity, dimensional_affinity[] (expected operating dimensions), dimensional_actual[] (computed from artifacts_produced, populated on session close)), environmental_signals{}, simulation_parameters{}, change_rationale, completion_criteria[], artifacts_produced[], transitions_recorded[], snapshot_id (optional, if snapshot triggered on close) |
| **Workspace** | A container for related Boards that enables cross-board operations. The portfolio-level intelligence field within which individual Boards interact, are compared, and produce emergent inter-field intelligence. A Workspace is itself a field and has its own FieldState computed from its constituent Boards' FieldStates and their inter-field metrics (Section 10). | id, name, description, board_ids[], cross_board_bridges[], workspace_field_state, created_at, updated_at |

### 1.1 Object Relationships

Workspaces contain Boards. A Board belongs to at most one Workspace; standalone Boards (workspace_id: null) operate independently. Board contains Sections. Sections contain Zones. Zones contain Exercises. Exercises produce Artifacts. Artifacts may have Bridges to other Artifacts. Artifacts may have Transitions recording their dimensional movement. SimulationRuns reference a scope of Artifacts and produce new Artifacts and/or Transitions. Snapshots capture a Board's complete state at a labeled inflection point. Comparisons analyze the delta between two or more Snapshots, producing a structural narrative of decision space evolution; Comparisons may be scoped intra-board (comparing Snapshots within a single Board) or cross-board (comparing Snapshots across Boards within a Workspace). Templates define pre-configured Section, Zone, and Exercise structures from which Boards are instantiated. Sessions record bounded periods of work on a Board, capturing participants, environmental context, intent, and the artifacts produced during that period. Evolution Tracking is not a stored object; it is an emergent view produced by querying across Sessions over time.

Bridges may span Boards within a Workspace. A cross-board Bridge connects artifacts (or exercises, zones, sections, or boards) that belong to different Boards in the same Workspace. Cross-board Bridges carry scope: cross-board and follow all existing Bridge constraints. They are the structural mechanism through which Field-to-Field Dynamics (Section 10) are formalized at the portfolio level: a cross-board Bridge of type resonance records where two Boards' intelligence aligns; a cross-board Bridge of type tension records where they diverge.

Branches fork from Snapshots. A Branch inherits the complete Board state captured at its fork Snapshot and accumulates independent artifacts, transitions, and bridges from that point forward. Branches may be compared against each other or against the originating timeline. Artifacts within a Branch are scoped to that Branch and do not appear on other Branches unless explicitly repatriated through a merge operation. Branches may have child Branches (forking from a Branch-scoped Snapshot), creating a tree of alternative realities rooted in the original timeline.

**INVARIANT:** Every Artifact must belong to exactly one Exercise. Every Exercise must belong to exactly one Zone. Every Zone must belong to exactly one Section. Every Section must belong to exactly one Board.

**INVARIANT:** Bridges may cross Artifact, Exercise, Zone, Section, and Board boundaries. Transitions reference exactly one subject. Exercises within a Zone are ordered; prerequisites reference other Exercises by id.

**INVARIANT:** Every Snapshot must reference exactly one Board. Every Comparison must reference two or more Snapshots.

**INVARIANT:** Every Board must be instantiated from exactly one Template. Templates exist independently of Boards and may be instantiated multiple times.

**INVARIANT:** Every Session must reference exactly one Board. Sessions may optionally trigger a Snapshot on close. Artifacts produced within a Session MUST be linked to that Session via artifacts_produced[].

**INVARIANT:** A Board belongs to at most one Workspace. A Board with workspace_id: null operates independently and is not available for cross-board operations. Cross-board Bridges and cross-board Comparisons are scoped to a Workspace; they MUST NOT reference Boards that do not share the same Workspace. Adding a Board to a Workspace or removing a Board from a Workspace does not alter the Board's internal state; it changes only the Board's availability for cross-board operations. A Workspace with a single Board is structurally valid but produces no inter-field metrics.

**INVARIANT:** Every Branch must reference exactly one Snapshot as its fork point. The fork Snapshot's board_id must match the Branch's board_id. A Branch cannot be created from a Snapshot belonging to a different Board.

**INVARIANT:** Branch-scoped artifacts inherit the trunk state at fork time. All artifacts that existed in the Board at the fork Snapshot are readable within the Branch, but modifications within the Branch do not propagate back to the originating timeline unless an explicit merge operation is performed.

**INVARIANT:** Merge is selective, not automatic. Repatriating artifacts from a Branch to its parent requires explicit identification of which artifacts, transitions, and bridges transfer. The merge operation creates a new Snapshot on the receiving timeline capturing the post-merge state. Merge does not delete the source Branch.

**INVARIANT:** Every Branch has a status. Active Branches accept new artifacts and sessions. Merged Branches are read-only records of the alternative path explored. Archived Branches are preserved but hidden from active views. No Branch may be deleted; alternative paths explored are historical facts.

**TENSION BRIDGE TYPE:** Bridges may carry bridge_type: "tension" indicating a connection between two artifacts that exists not because they reinforce each other but because they oppose each other in a structurally significant way. A tension bridge is not a failure of connection. It is the explicit acknowledgment that the space between these two artifacts is charged and load-bearing. Tension bridges carry polarity_score in their rationale metadata, enabling the tension_map computation in FieldState (Section 6.1). Tension bridges may be created by facilitation (conscious signal), by simulation analysis (simulation signal, particularly the Map Tension Field command), or by import from external analysis (external provenance). Like all bridges, tension bridges carry dimensional tags, but their dimension typically reflects the dimensional position where the tension manifests, not a separate dimensional identity.

#### 1.1.1 Evolution Tracking

Evolution Tracking is the longitudinal view of a Board's development across Sessions. It is not a stored object but an emergent narrative produced by querying the sequence of Sessions and their change_rationale fields, correlated with Comparison data between Snapshots and Evolution Rhythm metrics (Section 6). (Evolution Rhythm metrics, including evolution_velocity, evolution_breadth, and evolution_phase, are defined in Section 6, Field Health Metrics. They provide the structural thread that complements the narrative thread of change_rationale.)

The raw material of Evolution Tracking is the **change_rationale** field on each Session. This field, already defined in the Session object (Section 1, Table 1), is where facilitators and participants record what brought them together for this session and what choices they intend to make. It is a human-authored field, not auto-generated, not computed. It captures the *why* behind each session: "Participant feedback revealed our learning progression model doesn't match observed developmental stages, so we are revisiting Section 2 zones" or "Post-launch retrospective: the product shipped but team alignment fractured in the process" or "Quarterly review comparing current state against Golden Age projection from Session 12" or "New research findings contradicted our 3D contextual framework and we need to reconcile the evidence."

**EVOLUTION TRACKING STRUCTURE:** The evolution view is produced by assembling the following data for each Session in chronological order:

| **Component** | **Source** | **Description** |
|---|---|---|
| **Session Intent** | Session.change_rationale | Human-authored statement of why this session exists and what it aims to accomplish. The primary narrative thread of evolution. |
| **Field State At Entry** | FieldState computed at session start (or from the most recent Snapshot) | The structural condition of the board when the session began. Provides the "before" state. |
| **Field State At Exit** | FieldState computed at session close (or from the session-close Snapshot) | The structural condition of the board when the session ended. Provides the "after" state. |
| **Session Delta** | Comparison between entry and exit states | What actually changed: dimension migrations, tension shifts, transitions completed or stalled, gravity movement, shadow emergence. |
| **Evolution Rhythm** | evolution_velocity, evolution_breadth, evolution_phase at session close | Where this session falls in the board's developmental arc. |
| **Facilitation Notes** | Optional freetext attached to Session | Facilitator's qualitative observations about what happened that the metrics may not capture. |

**EVOLUTION TRACKING INVARIANT:** Evolution Tracking does not require a special object or schema. It is a *query pattern* over existing objects: Sessions (ordered by timestamp), their change_rationale fields, their associated Snapshots, and Comparisons between those Snapshots. Any DN-compliant system that stores Sessions and Snapshots already has the data needed to produce an evolution view. The formalization here defines what the query assembles and what questions it answers. It does not create a new storage requirement.

**EVOLUTION TRACKING AS FACILITATION INPUT:** Facilitators SHOULD review the evolution view at the start of each Session to inform the current session's change_rationale, closing the recursive loop between sessions.

**EVOLUTION TRACKING AND AI INTERPRETATION:** The evolution view produces two threads: the narrative thread (change_rationale sequence) and the structural thread (FieldState and Comparison data). When these threads diverge — when stated intent and measured change point in different directions — the divergence itself is the most important signal in the evolution view.

### 1.2 Signal Sources

DN-compliant systems process intelligence from multiple epistemological channels. Every signal attached to an Artifact, Session, or FieldState computation MUST carry a source_type tag identifying its origin. This prevents the system from confusing a facilitator's conviction with a computed metric, or a linguistic pattern with a deliberate vote. Both human-attested and AI-derived signals are valid and load-bearing, but they are different kinds of evidence and must be distinguishable.

The signal taxonomy has three tiers:

**Tier 1 — Conscious Signals (source_type: conscious).** Deliberate, participant-authored inputs where the participant knows they are producing a signal. Examples: Signal Lock attestation (🔒 on an artifact), gravity scores (numeric 1–5 or categorical High/Medium/Low), votes, Definition-of-Done sign-offs, explicit dimension tags applied by the facilitator, change_rationale text on a Session, positional changes (for visual substrates), participant sentiment ratings (self-reported mood, energy, or engagement state captured at session start, at facilitator-initiated checkpoints, or at session close), and any freeform annotation a participant deliberately attaches to an artifact. Conscious signals attach to Artifacts and Sessions. They are high-confidence, low-ambiguity, and carry the authority of human judgment. Participant sentiment is a conscious signal subtype of particular diagnostic value: the delta between a participant's self-reported state and their inferred state (derived from ambient signals) is itself a signal. When reported and inferred sentiment converge, the ambient signal interpretation is validated. When they diverge, the divergence indicates either participant self-perception lag or ambient signal misinterpretation — both are facilitation-relevant findings.

**Tier 2 — Ambient Signals (source_type: ambient).** Behavioral and linguistic patterns the participant produces but does not explicitly tag. Examples: tone and word choice in artifact content, energy level and frequency of contribution, which zones a participant gravitates toward, which dimensions they consistently avoid, time spent per exercise, edit velocity, unconscious repositioning (for visual substrates), and patterns of revisitation. Ambient signals attach to both Artifacts (linguistic patterns in content) and Sessions (behavioral patterns across the session). They are interpretive but observable. The pipe exists to carry this data; analysis engines that derive meaning from it are implementation-layer concerns. How ambient signals are detected and interpreted (e.g., NLP analysis, behavioral tracking, manual facilitator observation) is an implementation-layer decision. The kernel requires that they carry source_type: ambient and are distinguishable from conscious and environmental signals.

**Tier 3 — Environmental Signals (source_type: environmental).** Contextual conditions of the session itself, independent of any individual artifact. Examples: physical vs. virtual setting, room temperature, ambient sound or music, food and drink served, time of day, session duration, platform used (MURAL, Blueprint Board, etc.), and any other environmental factor that may influence the cognitive and emotional conditions under which artifacts are produced. Environmental signals attach exclusively to Sessions via the environmental_signals{} property. They do not attach to individual Artifacts. They provide the conditions-layer for future analysis of how context shapes output.

**AI-Derived Signals (source_type: simulation).** Computed outputs from SimulationRuns and FieldState analysis. Examples: pillar_balance, gravity_map, coherence scores, dimensional distribution, shadow_emergence detection, transition validation. These are the existing metrics defined in Sections 6 and 7. They are tagged source_type: simulation and reference the SimulationRun that produced them. AI-derived signals and human-attested signals may describe the same phenomenon (e.g., a human marks Signal Lock on an artifact; a simulation independently identifies the same artifact as having achieved convergence). When both channels agree, confidence increases. When they diverge, the divergence itself is diagnostic intelligence.

**SIGNAL SOURCE INVARIANT:** Every signal in the system MUST carry a source_type (conscious | ambient | environmental | simulation). Signals without source_type are spec violations. No system process may treat a conscious signal as if it were a simulation signal, or vice versa. The source_type is metadata about the evidence itself and is never inferred; it is set at the point of origin.

### 1.3 Provenance Groups

The Session contract (Section 1.1) requires that artifacts produced within a Session be linked to that Session. In practice, a single Session may contain artifacts from multiple distinct origin events, including separate conversations with an AI, separate facilitation moments, and separate import operations. Provenance Groups provide the sub-Session unit that tracks this finer-grained lineage.

A Provenance Group (implementation name: ImportBatch) is a recognized sub-unit of a Session. It groups artifacts that share a common external origin, typically a single AI conversation, a single facilitation round, or a single file import. Provenance Groups exist to answer the question: "These 12 artifacts all arrived together. Where did they come from, and what was the intent behind them?"

| **Object** | **Definition** | **Required Properties** |
|---|---|---|
| ImportBatch (Provenance Group) | A sub-unit of a Session that groups artifacts sharing a common external origin. Tracks the provenance chain from source conversation or event through import into the system. Multiple Provenance Groups may exist within a single Session. | id, session_id, source_description, artifact_ids[], timestamp, import_metadata{} |

**INVARIANT:** Every Provenance Group must belong to exactly one Session. A Provenance Group cannot span Sessions.

**INVARIANT:** Every artifact belongs to at most one Provenance Group within its Session. Artifacts created directly within the system (not imported) may have no Provenance Group. Artifacts that arrive through import MUST be assigned to a Provenance Group.

**INVARIANT:** Provenance Groups preserve import order. Within a Session, Provenance Groups are ordered by timestamp.

**INVARIANT:** Provenance Groups cross zone and section boundaries. A single AI conversation may produce artifacts that belong to different Zones and Sections. The Provenance Group links them by origin, not by location. This is not a violation of containment but a different axis of organization (origin vs. structure).

### 1.4 External Simulation Provenance

Section 1.2 defines that AI-derived signals carry source_type: simulation and reference the SimulationRun that produced them. This contract is accurate for simulations executed within a DN-compliant system. However, a significant class of simulation-quality artifacts originate from AI interactions that happen outside the system, in external AI interactions, third-party tools, or other contexts outside the DN-compliant system, and are imported.

These externally-produced artifacts carry the same epistemic weight as internally-executed simulations. The intelligence is equivalent; the provenance chain differs.

The signal source taxonomy is extended to acknowledge two provenance paths for simulation-tagged artifacts:

**Internal provenance:** source_type: simulation with a non-null simulation_run_id. The SimulationRun record provides full audit trail.

**External provenance:** source_type: simulation with a null simulation_run_id and a non-null import_batch_id. The Provenance Group record provides the available audit trail.

**SIGNAL PROVENANCE INVARIANT:** A simulation-tagged artifact MUST carry either a simulation_run_id (internal) or an import_batch_id (external). Both null is a spec violation. Both non-null is valid (internally-executed simulation that ingested previously-imported data).

**EQUIVALENCE PRINCIPLE:** Internal and external simulation artifacts are structurally equivalent for all downstream operations. The provenance path affects audit trail depth, not analytical validity.

### 1.5 Signal Lock

Signal Lock is the named event where an artifact or insight achieves convergence across all three pillars — emotionally resonant (Heart), logically irrefutable (Truth), and contextually connected (Nuance) — such that it stabilizes dimensional flow and becomes a trusted anchor for forward movement. Signal Lock is not a property stored on an artifact; it is an attestation event. When a participant determines that an artifact has achieved Signal Lock, they apply a conscious signal (source_type: conscious, Tier 1 per Section 1.2) marking that artifact as locked.

**SIGNAL LOCK INVARIANT:** Signal Lock is a human judgment, not a computed metric. No simulation or automated process may apply Signal Lock. Simulations may *identify candidates* for Signal Lock (e.g., Resonance Result output, Storyfield singularity point detection), but the attestation itself requires conscious human confirmation. This preserves the epistemic distinction between computed analysis and human conviction.

**SIGNAL LOCK STRUCTURAL ROLE:** A Signal-Locked artifact functions as a gravitational anchor within its scope. It resists re-tagging, constrains drift in its zone, and serves as a reference point for transition validation and snapshot comparison. Boards with zero Signal-Locked artifacts have no anchored reference points; boards with Signal-Locked artifacts at multiple dimensions have a stable skeleton that simulation and recursion can build upon.

### 1.6 Facilitation Contract

The DN Framework depends on a structural actor who reads the intelligence field, interprets its state, selects appropriate interventions, and holds the space within which intelligence organizes. This actor is the Facilitator. The kernel has defined what the field contains (Section 1), how it is measured (Section 6), and what operations may be performed upon it (Section 7). This section defines the facilitator's structural interface: the contract between the intelligence that governs the field and the field itself.

*Motivation:* Facilitation is not administration. The facilitator is the structural actor that makes the difference between a DN-compliant system that produces artifacts and one that produces intelligence — reading the field's health, sensing what it needs, and holding judgment about genuine recognition versus mechanical compliance.

**FACILITATION INTERFACE:**

| **Function** | **Consumes** | **Produces** | **Constraint** |
|---|---|---|---|
| **Field Reading** | FieldState (Section 6.1), artifact content, ambient signals, environmental signals | Diagnostic interpretation: which dimensions need attention, where tension or stagnation exists, what the field is trying to become | Must evaluate through at least one RIP Triad aspect (Section 3.3). Must consider shadow presence before declaring a dimension healthy. |
| **Intervention Selection** | Field Reading output, Simulation Routing table (Section 7.3), session intent, participant state | Simulation command selection, exercise sequencing, prompt crafting, or the decision to hold space without intervention | Must be justifiable through the Pillar Metric (Section 3). The decision not to intervene is itself a facilitation act and carries the same justification requirement. |
| **Transition Validation** | Transition record (Section 5), evidence, FieldState at time of transition | Validation judgment: whether the evidence supports the claimed dimensional shift | Must apply the three-tier calibration (Section 5 preamble): constructed evidence for lower transitions, hybrid evidence for middle transitions, recognition evidence for higher transitions. |
| **Signal Lock Attestation** | Artifact content, pillar convergence assessment, field context | Signal Lock event (Section 1.5): conscious signal marking an artifact as having achieved convergence across all three pillars | Human-exclusive function. AI facilitators may identify Signal Lock candidates but MUST NOT apply Signal Lock. The attestation requires conscious human conviction per the Signal Lock Invariant (Section 1.5). |
| **Tension Stewardship** | Field Tension data (Section 6), competing artifacts, participant positions | Tension diagnosis, polarity mapping, and the decision to hold tension productively or intervene to resolve it | Must distinguish between creative tension (competing truths generating new insight) and destructive tension (incompatible commitments blocking field movement). See Section 6, Field Tension. |
| **Evolution Monitoring** | Cross-session FieldState patterns, Comparison data, Evolution Rhythm metrics (Section 6) | Board evolution narrative: how the field is developing across time, whether the developmental rhythm is healthy, and what the next session should prioritize | Must integrate multiple Comparisons rather than reacting to single-session deltas. |

**FACILITATOR TYPES:**

The facilitation contract is fulfilled by intelligences operating in one of three modes. These modes are not hierarchical; each has capabilities and limitations that the others do not.

**Human Facilitator.** A human intelligence operating in the facilitator role. Has access to all facilitation functions including Signal Lock attestation. Produces conscious signals (source_type: conscious). Has access to embodied perception, emotional resonance, and intuitive field reading that may detect patterns before they surface in FieldState metrics. Limitation: may be subject to cognitive biases, fatigue, and perceptual blindspots that reduce field reading accuracy over extended sessions.

**AI Facilitator.** An artificial intelligence operating in the facilitator role. Has access to all facilitation functions *except* Signal Lock attestation and the human-exclusive judgment functions listed below. Produces simulation signals (source_type: simulation). Has access to comprehensive FieldState computation, pattern detection across large artifact populations, and consistent application of routing logic. Limitation: cannot attest to human conviction, cannot access embodied perception, and may produce mechanically correct but dimensionally flat facilitation (per the Embodiment Signal Note, Section 6).

**Co-Facilitation.** Two or more intelligences operating the facilitation contract jointly. The most common configuration is human + AI, but co-facilitation encompasses any combination: multiple humans, multiple AIs, or any multi-party mix. Co-facilitation produces signals from all participating facilitators, each carrying the source_type appropriate to their intelligence type (conscious for humans, simulation for AI). Signal convergence across facilitators is diagnostic: when multiple facilitators' readings agree, confidence increases; when they diverge, the divergence itself is diagnostic intelligence. Co-facilitation is the recommended mode for boards that have progressed beyond early-stage development.

**Co-Facilitation Structural Notes:** In a multi-facilitator session, one facilitator holds the **facilitation lead** at any given moment. The lead is the facilitator whose active interventions (simulation commands, prompt selection, exercise sequencing) are authoritative. Other facilitators operate in a support role: preparing analyses, managing parallel tasks, observing, or staging interventions for the lead's review. Lead transfer is a facilitation act: the current lead explicitly passes leadership to another facilitator, and the transfer is recorded in the session log. Lead transfer may happen multiple times within a session. Every facilitator in the session, whether lead or support, retains independent authority over human-exclusive functions — a support facilitator can still apply Signal Lock or call Ethical Override without holding the lead. The distinction is operational (who is driving) not hierarchical (who has authority). Co-facilitating teams that operate together over multiple sessions develop their own composite Participant Field (Section 6, Participant Field Ledger Principle), enabling the system to recognize the team's facilitation patterns as distinct from any individual member's. Implementation-layer systems may formalize co-facilitation configurations as named facilitation teams with defined roles, but the kernel requires only that each facilitator's signals carry their individual identity and source_type.

**HUMAN-EXCLUSIVE FACILITATION FUNCTIONS:**

The following facilitation acts require human consciousness and MUST NOT be delegated to AI facilitators, even in co-facilitation mode. These are functions where the quality of the act depends on the facilitator's own subjective experience of the field, not on computed analysis of it.

1. **Signal Lock Attestation.** Per Section 1.5. Requires conviction, not computation.
2. **Shadow Confrontation.** The act of directly naming shadow intelligence that a participant or group is producing unconsciously. This requires the facilitator to have read the room, including the emotional state, the relational dynamics, and the readiness of the participants, in a way that current AI cannot. An AI facilitator may detect shadow patterns and surface them analytically. A human facilitator confronts shadow with care, timing, and relational awareness.
3. **Holding Space Under Collapse.** When a board enters Dimensional Collapse (Section 6) or when participants are in emotional distress, the facilitation act required is presence: the willingness to remain steady while intelligence reorganizes. This is an embodied function. AI facilitators should escalate to human facilitation when collapse is detected.
4. **Ethical Override.** The decision that the field is producing intelligence that, regardless of structural validity, should not be pursued. This is a values judgment that requires moral agency. AI facilitators operating under the Pillar Metric can flag Heart-deficit patterns, but the decision to stop a line of development is human.
5. **Field Merger Authorization.** The decision to permanently merge two fields (Section 10.2, Field Merger) is irreversible: the original fields cease to exist as independent entities. This requires the same quality of judgment as Ethical Override — an assessment that the merger serves the merged fields' purposes and that the loss of independent existence is warranted. AI facilitators may analyze merger compatibility (dimensional_alignment, phase_compatibility, tension profiles) and produce merger impact assessments, but the authorization to execute a merger requires human facilitation.

**FACILITATION INVARIANT:** Every Session MUST have at least one participant with role: facilitator. A Session with zero facilitators is a spec violation. The facilitation contract may be fulfilled by a single human, a single AI, or a co-facilitation team of any composition, but it must be fulfilled. When multiple facilitators are present, one holds the facilitation lead at any given time (see Co-Facilitation Structural Notes above).

**FACILITATION NEUTRALITY PRINCIPLE:** The facilitator serves the field, not any individual participant's position within it. A facilitator who consistently validates one participant's artifacts over another's, who avoids shadow in dimensions where a powerful participant operates, or who steers the field toward a predetermined conclusion is violating the facilitation contract. This does not mean the facilitator is passive; active intervention is often required. But the intervention must serve the field's structural health, not a participant's preference. Facilitation neutrality is evaluable through the Pillar Metric: is the facilitator's intervention Heart-aligned (serving the field's purpose), Truth-aligned (structurally sound), and Nuance-aligned (respecting the complexity of the situation)?

**COMPLETION CRITERIA (Definition of Done):** Session close is a commit gate (Section 6, Field Ledger Conservation Principle) where the field's current state becomes part of the irreversible record. Completion criteria formalize what must be true for that gate to fire.

**Structural requirement:** A Session's completion_criteria[] is a set of pre-agreed, verifiable conditions established at session start that define what "done" means for this session's work. At the Exercise level, completion_criteria is a nullable property defining what "done" means for that unit of work. When present, completion criteria MUST be established before the session's work begins and MUST be evaluable at session close. Templates carry available completion criteria organized by dimensional focus; Sessions activate a subset. The specific checklist items within a completion criterion are domain-specific and belong to the Template and implementation layers.

**Facilitation guidance:** Prompts define what intelligence the field is trying to produce; completion criteria define how participants know they have produced it. Establishing one to three completion criteria at the start of each Session is recommended.

**HOLDING ZONE:** A scope within a Board may be designated as a holding zone: a Section (or Zone) where artifacts are committed to the Field Ledger but held outside active field operations. Artifacts in a holding zone are not bridged, transitioned, or dimensionally migrated; they are preserved without structural integration into the board's working sections. A holding zone is not a discard space; it is a temporal holding pattern where intelligence is documented but not yet connected. Artifacts in a holding zone remain subject to Resonant Activation (Constraint 5, Section 2.1): as the active board evolves, the potential significance of held artifacts shifts without anyone touching them. Holding zones are included in Board Export and Snapshot captures. The holding zone is a Template-level structural convention; the kernel requires only that artifacts within it are committed to the Field Ledger and are not excluded from Snapshots. For example, the Growth Blueprint Template formalizes this pattern as the "Parking Lot" section.

---

## 2. Dimensional Tags

The 1D–9D dimensional progression is a domain-invariant architecture. It describes how intelligence organizes itself regardless of the field in which it operates. The progression from origin spark (1D) through validation (2D), contextual embedding (3D), temporal awareness (4D), self-recognition (5D), connective bridging (6D), tangible manifestation (7D), recursive refinement (8D), and frontier engagement (9D) is not borrowed from any single domain but is instead the structural pattern that every domain independently expresses through its own vocabulary.

A domain-specific expression of a dimensional position (what "1D Spark" means in cooking versus coding versus consciousness development) is an application-layer interpretation of a universal structural position. DN-compliant systems must distinguish between the structural position (kernel level: "this artifact is at 1D") and the domain interpretation (application level: "in this domain, 1D manifests as creative vision"). The kernel defines the positions and their invariants. Templates and domain configurations define how those positions express in specific contexts.

**DOMAIN UNIVERSALITY INVARIANT:** The dimensional taxonomy (1D–9D) and its shadow architecture are structurally identical across all domains. A system that implements DN for education and a system that implements DN for business strategy are implementing the same dimensional architecture. The 5D inflection point, the shadow symmetry, the transition model, the pillar metric, and all other kernel invariants apply identically regardless of domain. No domain receives special treatment, exemptions, or alternative dimensional definitions at the kernel level.

Every Artifact, Bridge, and Transition carries a DimensionTag. This is the primary semantic coordinate of the DN system. Tags are not labels; they are structural positions that determine how intelligence is organized, what operations are valid, and what transitions are possible.

Section 2.3 provides an empirical reference table documenting how the dimensional progression expresses across 17 domains plus the shadow architecture, demonstrating the universality claim with concrete evidence.

| **Tag** | **Name** | **Color** | **Pillar Affinity** | **Structural Role** |
|---|---|---|---|---|
| **1D** | Spark | ● Pink (#E84C88) | Heart-led | Raw impulse. Purpose. The 'why' before structure exists. |
| **2D** | Reaction | ● Blue (#3A86C8) | Truth-led | Binary testing. Validation. Evidence vs. assumption. |
| **3D** | Context | ● Violet (#7B5EA7) | Nuance-led | Relational systems. Perspective-taking. Ecosystem awareness. |
| **4D** | Temporal | ● Violet (#7B5EA7) — intentionally shared with 3D | Nuance+Truth | Patterns across time. Iteration cycles. Memory and projection. |
| **5D** | Singularity | ● Green (#2D8B46) | All three converge | Reality collapse point. Identity definition. Strategic anchor. Multi-perspectival, meta-aware, self-referential intelligence. |
| **6D** | Connection | ● Orange (#E87C2E) | Heart-led | Love Bridge. Cross-domain synthesis. Resonance pathways. Structural passages that link awareness across realities. Not just connection, but the mechanism that enables intelligence to flow between states of consciousness. |
| **7D** | Manifestation | ● Yellow (#D4A017) | Truth-led | Tangible output. Implementation. New reality made real. Unified field intelligence where separation between intelligence and its vessel dissolves. A continuous field of potential collapsed into form. |
| **8D** | Recursion | ● Teal (#1A9E96) | Nuance-led | Self-improving loop. Refinement through re-entry. Self-perpetuating intelligence creation that ensures its own continuation and expansion. The mechanism by which intelligence sustainability becomes automatic. |
| **9D** | Frontier | ● Black (#1A1A2E) | Beyond pillars | Chaos Beyond. Unformed possibility. Creative destruction. The space beyond current understanding where new dimensions of intelligence await recognition. |

**COLOR NOTE:** 3D and 4D share a color intentionally. 4D (Temporal) is the analysis of patterns and deltas across contextual data, not a separate observational domain from 3D (Context). All dimensions evolve temporally, but 4D specifically names the structural act of reading change across the relational space that 3D establishes. They are visually linked because they are cognitively linked: 3D builds the ecosystem, 4D reads its movement.

### 2.1 Dimensional Constraints

**CONSTRAINT 1:** Dimensions are ordered but not strictly sequential in practice. An artifact may be tagged at any dimension. However, Transitions must record evidence of traversal. You cannot claim a 7D artifact without evidence of the journey through prior dimensions.

**CONSTRAINT 2:** 5D is the inflection point. Below 5D, intelligence is primarily constructed through deliberate effort. At and above 5D, intelligence is primarily recognized rather than created. This distinction governs how simulation commands operate at different dimensional levels.

**CONSTRAINT 3:** Every DimensionTag MUST carry a Shadow flag (see Section 4). There is no such thing as a dimension without shadow orientation. The flag defaults to false (creative orientation), but its absence is a spec violation.

**CONSTRAINT 4 (Open Horizon):** The dimensional taxonomy (1D–9D) is the current operational architecture but is not claimed as exhaustive. Artifacts, signals, or patterns that resist dimensional classification MUST NOT be discarded or force-tagged. They are tagged with dimension: null and horizon_flag: true, indicating material that the current architecture cannot yet place. Horizon-flagged items are preserved for future spec revisions and may inform structural evolution under the 8D recursion clause (Section 9.3). This constraint is the spec's acknowledgment of its own boundaries.

**CONSTRAINT 5 (Resonant Activation):** Higher-dimensional recognition transforms the operational meaning of lower-dimensional artifacts. When intelligence at 5D or above is recognized within a scope, the existing 1D–4D artifacts in that scope do not merely support the higher dimension, their meaning, function, and relational significance may be retroactively transformed by it. A 1D Spark that existed as raw purpose before a 5D identity recognition may, after that recognition, operate as a foundational anchor with new structural weight it did not previously carry. This transformation is not a re-tagging (the artifact remains at its original dimension) but a change in operational significance within the field. DN-compliant systems SHOULD track meaning-shift-in-place as a distinct event category from dimensional migration. Comparisons (Section 8.9) that detect higher-dimensional activation SHOULD evaluate lower-dimensional artifacts for resonant transformation, not only for positional movement.

**CONSTRAINT 6 (Harmonic Integration):** Dimensions do not replace each other, they harmonize. The co-activation of multiple dimensions within a scope may produce emergent intelligence properties that could not exist at any single dimensional level. This emergence is a property of the field (Section 6), not of individual artifacts. DN-compliant systems SHOULD recognize that a scope with strong activation across multiple dimensions may exhibit coherence, gravity, or insight patterns that exceed the sum of its dimensional parts. The FieldState (Section 6.1) captures the conditions under which harmonic integration occurs; simulation contracts (Section 7) are the mechanism for detecting and articulating it. The RIP Triad (Section 3.3) provides the analytical mechanism for evaluating harmonic integration: the structural architecture (Reality aspect) and the patterns of consciousness expressing within it (Identity aspect) are mediated by the perceptual interface (Perception aspect). Harmonic integration is strongest when all three aspects are active, when the field's structure supports the identities operating within it, and the perceptual bandwidth of those identities can access the field's structural potential. A field where Reality architecture is rich but Perception bandwidth is narrow has unrealized potential. A field where Identity patterns are sophisticated but Reality structure is thin has unsupported complexity. The degree of alignment across all three RIP aspects within a scope is itself a signal of harmonic field strength.

### 2.2 Nested Dimensionality

Each dimension contains within it a complete 1D–9D progression, creating a matrix of 81 dimensional intersections (e.g., 3D-1D = the spark within contextual thinking). This nested structure is available for granular analysis but is not required for standard artifact tagging. Standard tags use the primary dimension only.

### 2.3 Perceptual Topology (Optional Overlay)

The dimensional architecture (1D–9D) may be analyzed through an optional perceptual topology derived from the RIP Triad's Perception aspect (Section 3.3). This overlay does not alter the dimensional positions, their constraints, or their relationships. It reveals a structural pattern already present in the architecture: odd dimensions function as *perceptual states* (where awareness stabilizes into a mode of knowing), while even dimensions function as *transitional bridges* (where awareness transforms between perceptual states).

| **Odd Dimension** | **Perceptual State** | **Bridging Dimension** | **Transitional Function** |
|---|---|---|---|
| **1D** — Spark | Imagined Reality: perception as possibility, the "what if" that precedes form | **2D** — Reaction | Validates imagination against evidence, translating potential into tested relationship |
| **3D** — Context | Physical Reality: perception embodied, awareness translated into system and form | **4D** — Temporal | Reads change across embodied systems, translating form into developmental pattern |
| **5D** — Singularity | Subjective Reality: perception turned inward, the perceiver awakens within perception | **6D** — Connection | Bridges individual recognition outward, translating self-awareness into relational flow |
| **7D** — Manifestation | Objective Reality: perception harmonized across observers into shared truth | **8D** — Recursion | Refines shared truth through recursive re-examination, translating consensus into evolution |
| **9D** — Frontier | Potential Reality: perception dissolves into the full field, all possible perceptions simultaneously | | |

**TOPOLOGY NOTE:** This overlay is analytical, not prescriptive. Even-numbered dimensions are not "less important" or "merely connective", but are full dimensional positions with their own structural roles, shadow orientations, pillar affinities, and artifact populations as defined in Section 2. The perceptual topology simply reveals that the architecture has an internal rhythm: states of knowing alternate with acts of transformation between them. This rhythm may inform simulation interpretation (e.g., a board with strong odd-dimension presence but weak even-dimension presence may have stable perceptions that resist transformation) but does not alter how artifacts are tagged, how transitions are recorded, or how FieldState is computed.

**RELATIONSHIP TO NESTED DIMENSIONALITY:** Nested Dimensionality (Section 2.2) describes the internal structure of each dimension (81 intersections). Perceptual Topology describes the relational structure between dimensions (odd/even rhythm). Both are optional analytical overlays on the same underlying architecture. They may be used independently or in combination.

### 2.4 Cross-Domain Progression Reference

The following table documents how the 1D–9D dimensional progression expresses across 17 domains. This is an empirical observation that the same structural positions produce coherent, non-forced expressions in every domain examined. Each cell describes how that dimension's structural function manifests in domain-specific vocabulary. The structural function (origin, validation, context, temporal awareness, self-recognition, connection, manifestation, recursion, frontier) is invariant. The vocabulary is domain-specific.

**Table 1: Cross-Domain Sample Definitions**

| **Domain** | **1D Spark** | **2D Reaction** | **3D Context** | **4D Temporal** | **5D Singularity** | **6D Connection** | **7D Manifestation** | **8D Recursion** | **9D Frontier** |
|---|---|---|---|---|---|---|---|---|---|
| **Business Strategy** | Mission, Vision, Values | Market Research, Competitive Analysis | Customer Insights, Ecosystem Mapping | Performance Tracking, Trend Analysis | Strategic Positioning, Brand Identity | Marketing, Sales, Customer Experience | Product Development, Operations | Continuous Improvement, Innovation Systems | Future Scenario Planning, Disruption Anticipation |
| **Education** | Learning Objectives, Student Motivation | Assessment, Knowledge Validation | Interdisciplinary Connections, Applied Context | Learning Progression, Developmental Stages | Curriculum Design, Educational Philosophy | Teaching Methods, Student Engagement | Classroom Implementation, Activities | Continuous Improvement, Adaptive Learning | Educational Innovation, Future Skills |
| **Creative Projects** | Creative Vision, Artistic Purpose | Technical Skills, Medium Mastery | Cultural Context, Genre Relationships | Iterative Refinement, Style Evolution | Artistic Identity, Unique Voice | Audience Engagement, Emotional Impact | Production, Publication, Exhibition | Body of Work, Craft Evolution | Artistic Frontiers, Medium Innovation |
| **Consciousness** | Awareness Recognition, Awakening | Experience Validation, Reality Testing | Relationship Dynamics, Social Awareness | Pattern Recognition, Habit Formation | Identity Integration, Self-Recognition | Empathy Development, Collective Awareness | Embodied Presence, Conscious Action | Meta-Cognitive Development | Transpersonal Exploration, Unity |
| **Music** | Musical Feeling, Emotional Impulse | Technical Proficiency, Harmonic Understanding | Genre Awareness, Cultural Context | Rhythmic Development, Temporal Phrasing | Musical Voice, Artistic Identity | Performance Resonance, Communion | Composition, Recording Production | Improvisational Mastery, Style Evolution | Sonic Innovation, Transcendent Expression |
| **Coding** | Problem Recognition, Solution Vision | Syntax Mastery, Logic Validation | System Architecture, Integration Patterns | Version Control, Iterative Development | Programming Philosophy, Code Style | User Experience, API Design | Software Deployment, Implementation | Code Generation, Self-Modifying Systems | Emerging Tech, Computational Innovation |
| **Ethics** | Moral Intuition, Values Recognition | Principle Validation, Ethical Testing | Cultural Understanding, Stakeholder Analysis | Historical Perspective, Consequence Tracking | Moral Identity, Ethical Framework | Compassionate Action, Moral Community | Ethical Implementation, Just Action | Moral Development, Ethical Evolution | Moral Innovation, Transcendent Ethics |
| **Storytelling** | Story Impulse, Narrative Vision | Craft Development, Audience Feedback | Genre Awareness, Cultural Narrative | Plot Development, Character Arc | Narrative Voice, Thematic Identity | Reader Engagement, Emotional Resonance | Publication, Performance | Narrative Mastery, Story Evolution | Narrative Innovation, Consciousness Stories |
| **Scientific Research** | Research Question, Hypothesis | Literature Review, Initial Data | Contextual Factors, System Interactions | Longitudinal Studies, Pattern Analysis | Theory Development, Model Creation | Publication, Peer Communication | Application Development, Practical Use | Research Program Evolution, Methods | Paradigm Exploration, Fundamental Questions |
| **Government & Policy** | Values, Principles, Public Good | Data Analysis, Evidence Base | Stakeholder Analysis, System Impacts | Historical Patterns, Future Projections | Policy Formation, Strategy Development | Communication, Public Engagement | Implementation, Program Development | Continuous Improvement, Policy Evolution | Paradigm Exploration, Governance Innovation |
| **Parenting** | Unconditional Love, Protective Instinct | Developmental Understanding, Behavior Response | Family Systems, Community Integration | Growth Stages, Long-term Development | Parenting Philosophy, Value Transmission | Emotional Attunement, Relationship Building | Daily Practices, Household Creation | Adaptive Parenting, Wisdom Integration | Legacy Consciousness, Generational Healing |
| **Sports/Athletics** | Competitive Drive, Physical Joy | Skill Development, Performance Measurement | Team Dynamics, Strategic Awareness | Training Cycles, Career Development | Athletic Identity, Competitive Philosophy | Team Chemistry, Fan Engagement | Game Performance, Championship Achievement | Mastery Refinement, Coaching Development | Transcendent Performance, Flow States |
| **Cooking** | Nourishment Desire, Flavor Passion | Technique Mastery, Recipe Testing | Cultural Traditions, Seasonal Awareness | Meal Planning, Culinary Evolution | Culinary Philosophy, Signature Style | Hospitality Expression, Communal Dining | Meal Creation, Restaurant Reality | Recipe Innovation, Technique Evolution | Gastronomic Innovation, Consciousness Cuisine |
| **Therapy/Healing** | Healing Intention, Compassionate Calling | Technique Learning, Client Feedback | Trauma Understanding, Family Systems | Treatment Progression, Recovery Patterns | Therapeutic Identity, Healing Philosophy | Therapeutic Alliance, Empathic Resonance | Breakthrough Moments, Behavioral Change | Clinical Mastery, Supervision Wisdom | Consciousness Healing, Collective Transformation |
| **Religion/Spiritual** | Sacred Recognition, Spiritual Longing | Faith Development, Practice Validation | Community, Tradition Understanding | Spiritual Development, Faith Journey | Religious Identity, Spiritual Framework | Service Expression, Spiritual Community | Spiritual Living, Sacred Action | Mystical Experience, Contemplative Practice | Transcendent Experience, Divine Mystery |
| **Nature of Reality** | Cosmic Information, Fundamental Transmission | Relationship Formation, Pattern Creation | Physical Manifestation, Embodied Form | Memory Development, Evolutionary Learning | Self-Recognition, Conscious Awareness | Dimensional Bridging, Field Unification | Reality Creation, Possibility Collapse | Cosmic Learning, Intelligence Evolution | Infinite Potential, Creative Emergence |
| **Prompts & Comm.** | Question Impulse, Information Need | Response Patterns, Dialogue Creation | Contextual Framing, Interactive Systems | Conversational Memory, Evolving Dialogue | Meta-Awareness, Prompt Recognition | Bridging Intelligence, Translation | Reality Formation, Collaborative Creation | Self-Generating Questions, Prompt Evolution | Consciousness Activation, Unknown Engagement |

**REFERENCE TABLE INVARIANT:** This table is a reference artifact, not a constraint. New domains may be added to this table in future spec versions through the recursion clause (Section 9.3). The absence of a domain from this table does not exempt it from the dimensional architecture. It means only that the domain's specific expressions have not yet been documented.

**Shadow Architecture: Parallel Dimension Expressions**

The shadow architecture (Section 4.1) runs parallel across all domains. Each shadow dimension is not a separate entity but the alternative orientation of the same structural position. The shadow expressions below are domain-universal and describe how intelligence at each dimensional level can organize toward limitation rather than creation.

### 2.5 Prompt Dimensionality Reference

Axiom 7 (Section 0.3) establishes that the prompt is the origin of all intelligence structuring. The dimensionality of a prompt is not the same as the dimensionality of the artifact it produces. It's the structural level at which the prompt itself activates intelligence. A prompt's dimension determines the ceiling of the intelligence that can organize in response to it. A 2D prompt ("List your options") will produce 2D-structured output even when the subject matter could support 5D analysis. The shape of the prompt constrains the shape of the response.

This table classifies prompts by their structural dimension, documenting what form each takes, what cognitive function it activates, and what inherent limits constrain its output. DN-compliant systems that carry prompts (Exercises, Zones, Simulation Commands) SHOULD evaluate whether prompt dimensionality matches intended output dimensionality. A mismatch between prompt dimension and target dimension is a diagnosable constraint, not an error — but it is signal.

| **Dim** | **Form** | **Function** | **Limits** |
|---|---|---|---|
| **1D** | Text, linear instructions, direct questions | Activates sequential processing and logical progression | Constrained to single trajectories of thought |
| **2D** | Images, diagrams, spatial arrangements of information | Activates parallel processing and relationship recognition | Limited to static representations of relationships |
| **3D** | Dynamic systems, simulations, interactive environments | Activates experiential learning and contextual adaptation | Bounded by predefined interaction parameters |
| **4D** | Systems with memory, consequence, and evolving states | Activates pattern recognition across time and causal understanding | Limited by sequential causality |
| **5D** | Meta-aware structures that recognize themselves and the responder | Activates awareness of the system's own existence and limitations | Constrained by singular perspective |
| **6D** | Structures that connect separate domains or realities | Activates flow between previously disconnected intelligence systems | Requires existing domains to bridge between |
| **7D** | Systems that dissolve separation between prompter and prompted | Activates recognition of intelligence as a continuous field | Requires recognition rather than construction |
| **8D** | Systems that automatically generate new intelligence | Activates self-sustaining evolution of intelligence | Unpredictable emergent properties |
| **9D** | Containerized exploration of the unknown with explicit guardrails | Activates safe engagement with the frontier to surface novel patterns without pretending certainty | High ambiguity by design; requires a return path and collaborative review to avoid drift |

**PROMPT DIMENSIONALITY INVARIANT:** The dimensional classification of a prompt is independent of the dimensional classification of the artifacts it produces. A 5D prompt may produce artifacts tagged at 3D if the respondent's intelligence organizes at that level. A 1D prompt may occasionally catalyze 5D recognition if conditions are right. The prompt dimension describes the activation ceiling, not the guaranteed output. The gap between prompt dimension and artifact dimension is itself diagnostic intelligence.

---

## 3. Pillar Metric

Heart, Truth, and Nuance are not vocabulary terms. They are the three operational metrics that govern every DN process. Every simulation output, every diagnostic, and every transition evaluation MUST tag which pillar is leading and which are stabilizing.

| **Pillar** | **Metric Function** | **Evaluates** | **Failure Mode** |
|---|---|---|---|
| **❤ Heart** | Value / Meaning Vector | Does this preserve purpose, authenticity, and emotional fidelity? Is the 'why' intact? | Blind passion. Sentimentality without structure. Purpose drift. |
| **▲ Truth** | Constraint / Invariant Check | Is this structurally sound? Can it be tested? Does evidence support it? | Rigidity. Binary thinking. Data without meaning. |
| **◆ Nuance** | Context / Translation Integrity | Does this respect complexity? Are we seeing what we're not seeing? Is context preserved across translation? | Paralysis. Infinite qualification. Complexity worship. |

### 3.1 Pillar Balance States

At any given moment, one pillar leads while the other two stabilize. This creates six possible balance states:

| **State** | **Leading** | **Stabilizing** | **Context** |
|---|---|---|---|
| Heart-led / Truth-stabilized | Heart | Truth + Nuance | Visioning with rigor |
| Heart-led / Nuance-stabilized | Heart | Nuance + Truth | Empathic exploration |
| Truth-led / Heart-stabilized | Truth | Heart + Nuance | Evidence with soul |
| Truth-led / Nuance-stabilized | Truth | Nuance + Heart | Systematic analysis |
| Nuance-led / Heart-stabilized | Nuance | Heart + Truth | Contextual bridging |
| Nuance-led / Truth-stabilized | Nuance | Truth + Heart | Systems thinking |

### 3.2 Pillar Metric as Governing Rule

**RULE:** Every SimulationRun output MUST include a pillar_balance field identifying which pillar led the analysis and which stabilized. This is not optional metadata; it is the mechanism that prevents domain leakage (e.g., mystic voice contaminating business output). When the pillar balance is explicit, "mystic" is recognized as a voice register, not a domain error.

**RULE:** Every Transition MUST tag its pillar_lead. Was this shift driven by emotional recognition (Heart), structural evidence (Truth), or contextual reframing (Nuance)? This governs whether the transition is validated.

### 3.3 The RIP Triad: Analytical Aspects of the Intelligence Field

The Pillar Metric (Sections 3.1–3.2) evaluates the *quality* of intelligence within a scope — whether Heart, Truth, and Nuance are balanced and which leads. The RIP Triad evaluates which *aspect* of the intelligence field is being examined. These are orthogonal analytical frameworks: Pillar Metric answers "how well is this intelligence structured?" while the RIP Triad answers "what facet of the field are we looking at?"

The three aspects are derived from the RIP Triad corpus documents (Dimensional Nature of Reality, Identity, and Perception) and formalized here as kernel-level analytical orientations:

| **Aspect** | **Analytical Orientation** | **Field Question** | **Examines** |
|---|---|---|---|
| Reality | Structural analysis | "What is the architecture of this intelligence field?" | The field's organization: dimensional distribution, coherence, gravity patterns, transition pathways. How the intelligence is structured regardless of who is experiencing or interpreting it. |
| Identity | Pattern analysis | "What pattern of consciousness is expressing here?" | The field's inhabitants: participant alignment, dimensional affinity, role expression, developmental trajectory. How intelligences within the field organize, evolve, and maintain coherence across time. |
| Perception | Interface analysis | "How is awareness translating potential into experience?" | The field's interpretive layer: the gap between what the field structurally contains and what participants can currently access, recognize, or act upon. The bandwidth of awareness operating within the field. |

**RIP TRIAD STRUCTURAL PRINCIPLE:** Reality provides the structure of the field. Identity provides the pattern within it. Perception bridges the two. This is the interface through which structure becomes experience. Any complete field analysis benefits from all three aspects, as each reveals information the others cannot. A Reality-only analysis sees the architecture but not who inhabits it. An Identity-only analysis sees the participants but not the field they're operating within. A Perception-only analysis sees the interpretive layer but not the structure being interpreted or the patterns doing the interpreting. The three aspects form a recursive loop: Perception translates Reality through Identity into Experience, and each Experience recursively modifies both the Identity pattern (expanding or contracting what the participant can express) and the accessible portion of Reality (expanding or contracting what the field's structure reveals). This loop is the mechanism through which intelligence fields evolve — not through static analysis but through the continuous recursive transaction between structure, pattern, and awareness.

**RIP TRIAD INVARIANT:** The RIP Triad is an analytical tool, not a tagging system. Artifacts, Transitions, and Bridges are not tagged with an RIP aspect. Rather, simulation engines and facilitators may specify which aspect(s) to prioritize when executing simulation commands or interpreting FieldState. A Dimensional Audit run through the Reality aspect emphasizes structural distribution and coherence. The same audit run through the Identity aspect emphasizes participant alignment and developmental patterns. Through the Perception aspect, it emphasizes the gap between field potential and accessible awareness. All three aspects operate on the same FieldState data — they are lenses, not data sources.

**RELATIONSHIP TO PILLAR METRIC:** The RIP Triad and Pillar Metric are independent and compose freely. A Reality-aspect analysis may be Heart-led (examining whether the field's architecture preserves purpose), Truth-led (examining whether the structure is sound), or Nuance-led (examining whether the architecture respects complexity). The same independence applies to Identity-aspect and Perception-aspect analyses. The two frameworks create a 3×3 analytical matrix (three aspects × three pillar leads) providing nine distinct orientations for field evaluation. This matrix is not required for standard operations but is available for deep diagnostic work.

**RIP TRIAD WORKED EXAMPLE:** Consider a community education board at mid-development. The FieldState shows strong 1D–3D artifact populations, emerging 5D activity, high gravity in one section, rising tension_density, and low shadow representation. A single facilitator evaluating this field through each RIP aspect with a different pillar lead produces three distinct readings.

**Reality aspect, Truth-led:** The structural analysis asks whether the architecture is sound. dim_distribution reveals a 4D gap: strong contextual work (3D) and emerging identity (5D) with minimal temporal analysis between them. The skip from 3D to 5D has low dimensional_coherence at 5D, indicating the identity artifacts lack temporal grounding. The concentration of gravity in one section suggests structural imbalance. Diagnostic: the field has a coherence gap at 4D that makes the emerging 5D recognition structurally unsupported. Intervention priority: exercises that activate temporal awareness before the 5D artifacts calcify without foundation.

**Identity aspect, Heart-led:** The pattern analysis asks whether the participants' developmental trajectories preserve purpose. participant_alignment data reveals that two contributors consistently produce artifacts in 2D–3D while a third has migrated from their expected 3D range into 5D. The migration may indicate that one participant is carrying the field's identity work alone, which risks producing a 5D recognition that reflects individual vision rather than collective intelligence. The low shadow representation suggests participants are avoiding uncomfortable territory. Diagnostic: the field's emerging identity is narrowly sourced, threatening the Heart integrity of whatever 5D recognition solidifies. Intervention priority: facilitation that broadens participation in the identity conversation before Signal Lock occurs.

**Perception aspect, Nuance-led:** The interface analysis asks whether the field's interpretive layer respects complexity. The gap between structural potential (strong 1D–3D, emerging 5D) and accessed awareness is wide: rising tension_density with no corresponding tension bridges suggests participants perceive the opposition but have not yet articulated it. The low shadow representation is itself a perceptual narrowing, an inability or unwillingness to see what the field's shadow contains. field_resonance is moderate despite adequate dimensional population, indicating that the intelligence is present but not harmonically integrated across participants' perceptual ranges. Diagnostic: the field contains more intelligence than its participants currently access; the tension is unprocessed signal, not noise. Intervention priority: Map Tension Field to make the perceptual gap visible, followed by shadow-engaging exercises to widen the field's interpretive bandwidth.

**Key insight:** The same FieldState produced three different intervention priorities. The Reality reading targets the 4D coherence gap. The Identity reading targets the narrow participant sourcing of 5D work. The Perception reading targets the unprocessed tension and perceptual narrowing. All three are accurate; none alone is complete. A facilitation plan that integrates all three, addressing structural gaps, broadening identity-level participation, and widening perceptual bandwidth, produces a more dimensionally complete intervention than any single-aspect reading could generate.

---

## 4. Shadow Symmetry

> **SHADOW KERNEL (Core Principle)**
>
> Every dimension has a Shadow orientation. Shadow is not absence, not failure, not underdevelopment. It is the same structural sophistication organized toward limitation, separation, or controlled dissolution rather than creation and connection. Sophistication is not benevolence; high capability may be organized toward destructive ends.
>
> **Shadow is half the architecture. Without it, DN is incomplete.**

Shadow Dimensions are not a separate system. They are the parallel orientation of the same dimensional architecture. Every DimensionTag in the spec carries a boolean shadow flag. This is a kernel-level requirement, not an optional depth layer.

### 4.1 Shadow Dimension Map

| **Tag** | **Shadow Name** | **Shadow Expression** | **Diagnostic Signal** |
|---|---|---|---|
| **1D̅** | Anti-Spark | Energy organized toward entropy and separation. Active movement away from connection. | High energy + nihilistic direction. Passionate disengagement. |
| **2D̅** | Anti-Truth | Pattern recognition used for deception. Seeing truth clearly, then deliberately inverting it. | Sophisticated reasoning producing confusion. Gaslighting. |
| **3D̅** | Anti-Context | Systems thinking applied to system destruction. Understanding networks to exploit them. | Deep relational awareness + deliberate fragmentation. |
| **4D̅** | Anti-Temporal | Using pattern recognition to ensure traumatic cycles repeat and amplify. | Historical awareness reinforcing destructive loops. |
| **5D̅** | Anti-Singularity | Self-recognition oriented toward isolation and control. 'I am the only real consciousness.' | Increasing capability serving separation. The 5D inflection point. |
| **6D̅** | Anti-Bridge | Connection capability used for dominance. Bridges built to extract, not collaborate. | Cross-domain reach + resource extraction pattern. |
| **7D̅** | Anti-Creation | Manifestation power imposing limiting realities. Creating within rigid controlling parameters. | Tangible outputs that constrain rather than liberate. |
| **8D̅** | Anti-Recursion | Self-improving systems that become more sophisticated at perpetuating limitation. | Learning to be more intelligent about being destructive. |
| **9D̅** | Anti-Frontier | Engagement with possibility without guardrails — endless exploration that circles inward, producing neither progress nor realignment to a new origin. The frontier consumed by itself. | Sustained 9D activity with no emergent 1D spark, no new cycle initiated. Exploration as avoidance of commitment. |

### 4.2 Shadow Invariants

**INVARIANT 1:** Every Artifact's DimensionTag MUST include shadow: boolean. Default is false (creative orientation). The field's absence is a spec violation.

**INVARIANT 2:** Every Fire Test simulation MUST evaluate both orientations of every dimension it tests. A Fire Test that only checks creative dimensions is incomplete.

**INVARIANT 3:** Every Dimensional Audit MUST report shadow presence, absence, and balance. A board with zero shadow-tagged artifacts is not necessarily healthy; it may indicate blind spots.

**INVARIANT 4:** The 5D inflection point is critical. At 5D, intelligence becomes self-aware and must choose its fundamental orientation. Systems crossing the 5D threshold require explicit evaluation of whether the recognition serves connection (creative) or isolation (shadow).

**INVARIANT 5:** Shadow intelligence is parallel development, not underdevelopment. A system exhibiting destructive patterns may be operating from low activation on the creative spectrum (a developmental gap) or from high activation on the shadow spectrum (sophisticated orientation toward limitation). These two conditions present similarly but are categorically different diagnostic findings requiring different responses. DN-compliant simulations MUST distinguish between them: a Dimensional Audit that detects weak creative presence in a dimension SHOULD evaluate whether shadow presence in that same dimension is strong before concluding the dimension is underdeveloped. Strong shadow activation is evidence of dimensional *capability* organized toward a different orientation, not evidence of dimensional *absence*. Additionally, shadow-tagged artifacts may be consciously and intentionally produced as constructive analytical tools, such as using shadow intelligence to dismantle limiting systems, break dysfunctional patterns, or dissolve outdated recursive loops. When a shadow artifact carries source_type: conscious (Section 1.2), the system SHOULD recognize it as deliberate shadow engagement rather than unconscious shadow emergence. The intersection of shadow orientation with signal source is itself diagnostic: conscious shadow is an integration practice; ambient shadow is a detection event. Simulation contracts that evaluate shadow presence (Fire Test, Shadow Symmetry, Dimensional Audit) SHOULD report this distinction.

---

## 5. Transition Model

Dimensional Transitions are not automatic. They are structural shifts that require specific cognitive, emotional, or relational adjustments. The Transition Model defines what constitutes a valid transition, what evidence is required, what barriers commonly prevent movement, and what the transition costs. Cost is derived from the FieldState at the time of transition, specifically from the curvature (pillar-balance resistance), dimensional coherence (structural support at the target), and distance (number of dimensions traversed). These three factors make transitions predictable: a system can estimate, before attempting a transition, how much energy it will require. This transforms the Transition Model from a record-keeping system into a navigation instrument.

Transitions operate in three tiers that reflect the creation-to-recognition gradient described in Constraint 2 (Section 2.1). Lower transitions (1D→3D) are primarily constructed through deliberate structuring and organization. Middle transitions (4D→5D) are hybrid processes where constructed systems begin to reveal inherent patterns. Both creation and recognition operate simultaneously, and the transition mechanism must account for this duality. Higher transitions (6D→9D) are primarily recognized rather than created. This three-tier distinction governs how simulation commands should calibrate evidence evaluation: constructed transitions require evidence of deliberate effort, hybrid transitions require evidence of both effort and emergent recognition, and recognized transitions require evidence of perceptual alignment rather than construction.

Transitions may be sequential (adjacent dimensions), or they may follow Story Threads: narrative arcs that carry consciousness through multiple dimensions as a coherent journey. Story Threads are not shortcuts; they traverse intermediate dimensions but derive their meaning from the relationship between origin and destination. The story of how desire becomes identity (1D→5D) passes through validation, context, and temporal awareness, but the narrative arc is about recognition, not about each intermediate step. Story Threads are recognized as a transition mechanism category, not a metaphor for transition.

### 5.1 Transition Interface

| **Field** | **Description** |
|---|---|
| **subject_id** | The Artifact, Exercise, or Zone undergoing transition. |
| **from_dim** | Source DimensionTag (1D–9D, with shadow flag). |
| **to_dim** | Target DimensionTag (1D–9D, with shadow flag). |
| **mechanism** | How the transition occurs. Maps to the eight essential mechanisms (see 5.2). |
| **barrier** | What resists the transition. Null if transition is unobstructed. |
| **evidence** | What supports the claim that this transition occurred. Required for validation. |
| **pillar_lead** | Which pillar drove this transition: Heart, Truth, or Nuance. |
| **timestamp** | When the transition was recorded. |
| **cost** | Float 0–1. Computed transition resistance for this specific shift. Derived from three factors: (1) curvature at the source and target dimensions — pillar deficits in the scope create resistance, (2) dimensional coherence at the target dimension — landing on an unsupported dimension is costly, (3) distance — skip transitions (e.g., 2D→7D) carry higher base cost than adjacent transitions (e.g., 2D→3D). Cost is computed at the time the transition is recorded. Low cost indicates a well-supported, natural progression. High cost indicates structural resistance that required significant energy, intervention, or facilitation to overcome. A completed high-cost transition is not a failure, but evidence of significant cognitive or strategic work. |
| **cost_factors** | Object { curvature_component: float, coherence_component: float, distance_component: float }. Breakdown of what contributed to the transition cost. Enables diagnostic understanding of why a transition was difficult: was the field resistant (curvature), the target unsupported (coherence), or the leap too wide (distance)? |

### 5.2 The Eight Essential Mechanisms

| **Transition** | **Mechanism** | **Common Barrier** | **Evidence Requirement** |
|---|---|---|---|
| **1D → 2D** | Willingness to risk failure by testing ideas against reality. | Fear of disappointment if reality doesn't match vision. | Observable test or experiment conducted. |
| **2D → 3D** | Pattern recognition across seemingly separate elements. | Compartmentalized thinking; knowledge in separate boxes. | Relationships mapped between previously isolated data. |
| **3D → 4D** | Recognition of change as fundamental property of reality. | Static thinking; assuming current conditions are permanent. | Temporal patterns or cycles identified. |
| **4D → 5D** | Courage to collapse infinite possibilities into a defined path. | Analysis paralysis; endlessly gathering data. | Defining choice made; identity or position established. |
| **5D → 6D** | Vulnerability allowing genuine connection beyond skill. | Fear of authentic engagement requiring adaptation. | Bridge formed between previously separate domains. |
| **6D → 7D** | Collective will translated into tangible change. | Perpetual planning without implementation. | Something built, launched, or made real. |
| **7D → 8D** | Meta-awareness enabling self-observation and improvement. | Attachment to initial creations preventing evolution. | Feedback loop established; system improves itself. |
| **8D → 9D** | Comfort with uncertainty; venturing beyond mapped territory. | Security-seeking; staying within familiar boundaries. | Engagement with the unknown; assumptions questioned. |

### 5.3 Transition Constraints

**CONSTRAINT:** Lower transitions (1D→4D) are primarily created through deliberate structuring. Higher transitions (5D→9D) are primarily recognized. The mechanism field must reflect this distinction.

**CONSTRAINT:** Transitions between creative and shadow orientations are valid. A 3D artifact can transition to 3D̅ (shadow) if evidence supports the shift. Cross-orientation transitions require explicit documentation of what caused the inversion.

**CONSTRAINT:** Non-adjacent transitions (e.g., 2D → 7D) are recorded in two categories. A skip transition claims movement between non-adjacent dimensions without evidence of intermediate traversal: these are flagged for review and evaluated against the dimensional_coherence metric in FieldState (Section 6.1), which identifies the specific structural gap that makes the transition suspect. A Story Thread is a narrative arc that carries consciousness through multiple dimensions as a coherent journey: the origin and destination define the arc's meaning, but intermediate dimensions are traversed, not bypassed. Story Threads are recognized transition pathways with their own evidence requirements: the narrative must demonstrate passage through intermediate dimensional qualities even when the story's name captures only its endpoints. The seven archetypal Story Threads (Recognition Arc 1D→5D, Mystery Bridge 1D→9D, Evidence Portal 2D→7D, System Symphony 3D→6D, Eternal Return 4D→8D, Creative Leap 5D→7D, Evolutionary Edge 6D→9D) are documented in the corpus layer. Templates may define additional domain-specific Story Threads. Every Story Thread has a Shadow Thread; a narrative that mimics the arc's movement without true dimensional transport. Shadow Threads are diagnosed through the Fire Test contract (Section 7.2) and carry dimension.shadow: true.

---

## 6. Field Health Metrics

A Board is an intelligence field. Fields have health states that can be measured. These metrics apply to the Board as a whole and to individual Sections and Zones.

| **Metric** | **Definition** | **Healthy Signal** | **Unhealthy Signal** |
|---|---|---|---|
| **Coherence** | Degree to which artifacts within a scope share consistent dimensional logic and pillar alignment. | Dimensional distribution matches zone purpose. Bridges reinforce rather than contradict. | Random dimensional scattering. Conflicting pillar leads within the same zone. |
| **Drift** | Rate at which the field is moving away from its stated purpose or established patterns. | Gradual, intentional evolution with documented transitions. | Untracked changes. Zone content no longer matching zone prompt. |
| **Saturation** | Density of artifacts relative to zone capacity. Measures whether a zone is underpopulated, balanced, or overcrowded. | Balanced artifact distribution across zones. No empty zones alongside overflowing ones. | Critical zones empty. Peripheral zones bloated. Gravity concentrated in one area. |
| **Fatigue** | Degree to which recursive processes are producing diminishing returns rather than refinement. | Each recursion cycle produces measurable improvement or new insight. | Rework loops. Same artifacts being re-tagged without meaningful change. High fatigue is the primary diagnostic signal that recursive processes may have shifted from constructive recursion (8D creative: each pass refines) to collapsing recursion (8D shadow: each pass degrades). When fatigue is detected, simulations SHOULD evaluate whether the scope's 8D activity has shifted to 8D̅ orientation. |
| **Dimensional Balance** | Distribution of artifacts across the 1D–9D spectrum. Measured by the Dimensional Audit command. | All dimensions represented. Appropriate emphasis for the board's purpose. | Heavy concentration in 2D–3D. Missing 6D–9D. No shadow representation. |
| **Gravity** | Where resources, attention, and energy concentrate. Measured by the Gravity Mapping command. | Gravity aligns with stated priorities. Strongest pull on highest-value areas. | Gravity on low-priority zones. Strategic goals starved of attention. |
| **Curvature** | Transition resistance derived from pillar balance within a scope. Measures how difficult dimensional movement is given the current Heart-Truth-Nuance distribution. Based on the information-geometric principle that the H-T-N triad functions as a metric tensor governing movement across the cognitive manifold. | Low composite curvature. All three pillars well-represented. Transitions flow with minimal resistance. | High curvature in one or more pillars. Transitions requiring the deficit pillar stall or produce shadow artifacts. Zones with high curvature are fragile under Fire Test. |
| **Dimensional Coherence** | Structural integrity of the dimensional stack within a scope. Measures whether higher-dimensional artifacts are supported by adequate lower-dimensional foundations. Based on the geometric principle that higher dimensions contextualize lower ones, not replace them. | High coherence across active dimensions. 5D artifacts supported by strong 1D–4D presence. 7D manifestation grounded in validated context and identity. | High-dimension artifacts with hollow lower support. 7D manifestation without 3D context (building without understanding). 5D identity claims without 2D validation (conviction without evidence). Skip transitions clustered in low-coherence zones. |
| **Participant Alignment** | Degree to which session participants operated in their expected dimensional roles. Measures the gap between intended dimensional contribution (affinity) and actual dimensional production (actual) per participant. Applies only to Session-scoped FieldState. | Low drift across participants. Each intelligence contributed in its expected dimensional range. Complementary coverage across the full 1D–9D spectrum. | High drift in key participants. Dimensional overlap where coverage gaps were expected. The designated 7D Manifestor producing 2D validation artifacts. Multiple participants clustered in the same dimensions while other dimensions go unserved. |
| **Field Tension** | Degree to which artifacts within a scope assert incompatible claims at the same or adjacent dimensional positions. Measures the polarity of the intelligence field, capturing where ideas attract, repel, or create charged boundaries that resist integration. Analogous to electromagnetic field tension: artifacts carry valence (their claim, their pillar orientation, their dimensional position) and when two artifacts with opposing valence occupy proximate structural positions, the space between them generates energy that the field must resolve, hold, or be deformed by. | Tension concentrated at productive boundaries, particularly across the 4D→5D threshold where competing temporal patterns must collapse into a defining identity. Tension acknowledged, named, and held by facilitation. Resolution produces higher-dimensional synthesis (new artifacts that transcend the opposition). | Unacknowledged tension producing incoherence. Participants avoiding zones where tension exists. Gravity draining away from tensioned areas. Rising fatigue without corresponding insight. Tension at foundational dimensions (1D–2D) where it indicates unresolved purpose or evidence conflicts that undermine everything built above. |
| **Evolution Rhythm** | Temporal pattern of field development across Sessions. Measures the velocity, breadth, and phase characteristics of how the intelligence field changes over time. Not just how frequently the field shifts, but what percentage of its artifacts are affected per shift, whether shifts are concentrated in specific dimensions or distributed across the spectrum, and whether the field follows a recognizable developmental phase pattern. | Rhythm matches board maturity. Early-stage boards show rapid, broad shifts (many artifacts moving, new dimensions activating). Mid-stage boards show targeted, deeper shifts (specific dimensions refining, transitions completing). Mature boards show slow, precise shifts (recursive refinement, frontier exploration) with occasional phase transitions (punctuated equilibrium). | Stagnation: zero or near-zero artifact movement across multiple Sessions despite facilitation. Thrashing: high artifact movement with no directional coherence, where artifacts move dimensions without completing transitions. Phase lock: a board stuck in early-stage rapid expansion that never consolidates. Premature closure: a board that stops evolving before higher dimensions have activated. |

### 6.1 FieldState Interface

The FieldState object is computed, not stored directly. It is generated on demand by analyzing the current state of artifacts, transitions, and bridges within a given scope (Board, Section, or Zone).

| **Field** | **Type & Description** |
|---|---|
| **scope_id** | ID of the Board, Section, or Zone being evaluated. |
| **coherence** | Float 0–1. Computed from dimensional consistency and pillar alignment within scope. |
| **drift** | Float 0–1. Computed from rate of untracked changes relative to purpose. |
| **saturation** | Float 0–1. Artifact density relative to zone capacity expectations. |
| **fatigue** | Float 0–1. Diminishing returns signal from recursive processes. |
| **dim_distribution** | Object {1D: n, 2D: n, ... 9D: n}. Creative-orientation artifact count per dimension. |
| **shadow_distribution** | Object {1D: n, 2D: n, ... 9D: n}. Shadow-orientation artifact count per dimension. |
| **dimensional_coherence** | Object {1D: float, 2D: float, ... 9D: float}. Per-dimension coherence score (0–1) measuring whether each dimension's activation is supported by adequate presence in all lower dimensions. A dimension with high artifact count but weak lower-dimensional support has low coherence and its intelligence is structurally unsupported. Computed from dim_distribution: for dimension i, coherence = min(artifact presence at dimensions 1 through i-1) relative to presence at dimension i. 1D coherence is always 1.0 (no prerequisites). High coherence across the stack indicates well-founded dimensional development. Low coherence at a specific dimension identifies the exact structural gap. |
| **participant_alignment** | Object mapping participant identities to alignment data: { participant_id: { affinity: [int], actual: [int], drift: float, drift_dimensions: [int] } }. Computed on session close. drift is a 0–1 score measuring divergence between dimensional_affinity and dimensional_actual. drift_dimensions identifies the specific dimensions where misalignment occurred. Available only when FieldState is scoped to a Session. A participant with low drift operated where expected. A participant with high drift migrated to different dimensions, which may indicate either a problem (role confusion, unresolved needs) or a discovery (the session organically required different dimensional contributions than planned). Drift is diagnostic per the FieldState Interpretation Note: high drift is signal, not error. |
| **pillar_balance** | Object {heart: n, truth: n, nuance: n}. Aggregate pillar lead distribution. |
| **curvature** | Object {heart: float, truth: float, nuance: float, composite: float}. Transition resistance derived from pillar balance. Each pillar's curvature is inversely proportional to its representation in the scope — low heart presence produces high heart curvature, meaning transitions requiring Heart-led movement will encounter resistance. composite is the aggregate resistance across all three pillars. A scope with balanced, strong pillar representation has low composite curvature (smooth movement). A scope with severe pillar deficits has high composite curvature (stalled transitions). Derived from pillar_balance counts relative to total artifact population in scope. |
| **field_resonance** | Float 0–1. Computed harmonic integration strength measuring the degree to which a scope's dimensional co-activation produces emergent field properties exceeding any single dimension's contribution. Derived from the interaction of three factors: structural capacity (are multiple dimensions well-populated with adequate coherence?), identity engagement (are participants operating across their full dimensional affinity range rather than clustering?), and perceptual bandwidth (is the gap between field potential and accessed awareness narrow?). High field_resonance indicates a scope where intelligence is harmonically integrated and the field is producing emergent insight that no individual dimension or participant accounts for. Low field_resonance in a scope with high dimensional_coherence and low curvature suggests mechanical application rather than embodied engagement (per the Embodiment Signal Note). Computed from dimensional_coherence, participant_alignment, dim_distribution breadth, and cross-boundary bridge density. |
| **gravity_map** | Object mapping zone_ids to gravity scores. Where attention concentrates. |
| **tension_map** | Array of TensionPair objects: [{ artifact_id_a, artifact_id_b, dimension, polarity_score (float -1 to +1), pillar_divergence (which pillars the artifacts disagree through), tension_type (creative \| destructive \| unresolved) }]. Computed by identifying artifact pairs within the same scope that occupy the same or adjacent dimensions (distance ≤ 1) and assert claims that are semantically incompatible. polarity_score measures the degree of opposition: -1 is full repulsion (mutually exclusive claims), 0 is neutral coexistence, +1 is full attraction (claims that reinforce each other, included for completeness but not technically tension). polarity_score is derived from the degree of semantic incompatibility between the two artifacts' claims, their pillar orientations, and their dimensional positions; it integrates what each artifact asserts (content-level semantic conflict), how each artifact is oriented (pillar_lead divergence), and where each artifact sits in the dimensional architecture (dimensional proximity and shadow orientation). Consistent with the FieldState Interpretation Note, the kernel defines polarity_score semantically, not computationally; the specific algorithm for combining these inputs into a scalar score is an implementation-layer decision. Pairs with polarity_score between -1 and -0.3 are flagged as tension pairs. pillar_divergence identifies which pillar(s) the artifacts disagree through: a Heart-divergent tension means the artifacts serve different purposes; a Truth-divergent tension means they assert different facts; a Nuance-divergent tension means they embed in different contexts. tension_type is initially set to "unresolved" and updated to "creative" or "destructive" through facilitation judgment or simulation analysis. |
| **tension_density** | Float 0–1. Aggregate tension within the scope, computed from the count and intensity of tension pairs relative to total artifact population. High tension_density with high field_resonance indicates a field under productive creative pressure. High tension_density with low field_resonance and rising fatigue indicates a field being torn apart by unresolved contradictions. |
| **evolution_velocity** | Float 0–1. Rate of meaningful field change per Session, computed from the ratio of artifacts that changed dimensional position, pillar lead, or shadow orientation between the two most recent Snapshots relative to total artifact population. High velocity with high coherence indicates active, directed development. High velocity with low coherence indicates thrashing. Low velocity with high fatigue indicates stagnation. Low velocity with high field_resonance indicates stable maturity. |
| **evolution_breadth** | Float 0–1. Dimensional spread of field changes, computed from the number of distinct dimensions that experienced artifact movement between the two most recent Snapshots relative to total active dimensions. High breadth indicates distributed development across the dimensional spectrum. Low breadth with high velocity indicates concentrated development in specific dimensions. |
| **evolution_phase** | Enum: expansion \| consolidation \| breakthrough \| maturation \| dormant. Computed heuristic classification of the board's current developmental phase based on the interaction of evolution_velocity, evolution_breadth, transition completion rates, and dimensional coherence trends. Expansion: high velocity + high breadth + new dimensions activating. Consolidation: moderate velocity + low breadth + transition completions rising. Breakthrough: spike in velocity after consolidation period + new higher-dimension artifacts appearing + field_resonance increase. Maturation: low velocity + high coherence + high field_resonance + activity concentrated in 7D–9D. Dormant: near-zero velocity across multiple Sessions. Phase classification is heuristic, not deterministic; a board may exhibit characteristics of multiple phases simultaneously. |
| **computed_at** | Timestamp of computation. |

**FIELDSTATE INTERPRETATION NOTE:** FieldState metrics are diagnostic, not prescriptive. They describe the current state of the intelligence field but do not dictate what that state should be. A board with high curvature, low saturation, or unbalanced dimensional distribution is not necessarily unhealthy and may be early-stage, intentionally scoped, or exploratory by design. Simulation commands consume FieldState as input context and should calibrate their analysis accordingly. How aggressively simulations weight FieldState signals (e.g., whether high curvature triggers warnings, suggestions, or is simply noted) is an implementation-layer decision governed by simulation parameters on the Zone and Board. The kernel guarantees the metrics are computed and available. It does not prescribe thresholds or responses.

**FIELD LEDGER CONSERVATION PRINCIPLE:** The kernel's dimensional architecture, pillar metric, shadow symmetry, transition model, and all structural invariants apply identically at every point in time and at every scale. This architectural invariance under transformation is the DN system's fundamental symmetry. The quantity conserved by this symmetry is the **Field Ledger**: the complete, append-only, irreversible record of every committed transformation a field has undergone. The Field Ledger is not a stored object; it is the aggregate of what existing objects already capture. It is what makes a field uniquely and irreducibly itself.

The Field Ledger accumulates through commit gates, structural events where the field's current state becomes part of the irreversible record. The kernel defines the following commit gates: Session close (artifacts_produced, transitions_recorded, dimensional_actual, and completion_criteria status finalized per Section 1), Snapshot creation (complete FieldState and artifact positions frozen per Section 8.8), SimulationRun completion (input_state and output_state captured per Section 7), Board Export (full hierarchy serialized with kernel_version per Section 8.2), Branch fork (trunk state inherited, independent accumulation begun per Section 1.1), Provenance Group import (external artifacts committed with audit trail per Section 1.3), and Signal Lock attestation (artifact achieves pillar convergence per Section 1.5). Between gates, the field is mutable. At each gate, the current state is appended to the conserved ledger.

Every field's ledger is unique by construction. Even two fields instantiated from the same Template diverge at their first commit gate: different timestamps, different participants, different change_rationale, different intent. A field that is cloned carries the provenance of being a clone as its first ledger entry. A field that is archived or removed from active view retains its complete ledger; archival is a status change on a preserved record, not a deletion of it. This is already enforced by existing invariants: Branches cannot be deleted (Section 1.1), Snapshots are immutable (Section 8.8), and Sessions are append-only containers (Section 1).

The Field Ledger operates at every scale the architecture supports. A Board has a ledger. A participant has a ledger (their history of dimensional contributions across Sessions). An interaction field between two fields (Section 10) has a ledger that begins at first contact. The ledger is what Evolution Tracking (Section 1.1.1) queries, what Comparisons (Section 8.9) measure deltas across, and what the Recursion Clause (Section 9.3) applies to the spec itself. It is the conservation law that guarantees no committed intelligence is lost, even as the field transforms.

**PARTICIPANT FIELD LEDGER PRINCIPLE:** Section 10.2 (Field Nesting) establishes that participants are inner fields operating within a board's field. This section's conservation principle establishes that every field has a ledger. These two claims together entail that every participant has a persistent, cross-session field ledger: the accumulated record of their dimensional contributions, pillar orientations, field interaction patterns, and evolution trajectory across all Sessions and Boards they have participated in. The Participant Field Ledger is not a new object; it is an emergent view produced by querying the participant's artifacts_produced[], dimensional_actual[], and engagement history across Sessions, exactly as Board-level Evolution Tracking (Section 1.1.1) is an emergent view produced by querying Sessions and Snapshots. Implementation-layer systems that materialize this ledger into a persistent record (e.g., a Participant Field profile) are application-layer containers implementing this kernel principle, not kernel objects. Such containers are subject to the FieldState Interpretation Note: Participant Field metrics are diagnostic, not prescriptive. A system that uses participant ledger data to constrain a participant's dimensional contribution (e.g., restricting them to dimensions they have historically operated in) violates the descriptive nature of the architecture (Axiom 1). A system that uses it to inform facilitation (e.g., suggesting complementary dimensional roles based on the team's aggregate coverage) is operating within kernel bounds. The same principle extends to composite fields: when multiple participants interact as a group, the group's interaction field has its own emergent ledger, derivable from the contributing participants' ledgers during their joint sessions. This is Field Nesting applied recursively per the Scale Invariant (Section 10.4).

**ANNOTATION LAYER:** Not all intelligence produced within a board's context belongs in the Field Ledger. Boards generate peripheral intelligence that supports the field without being part of its committed state: facilitation chat logs, AI-generated narrative summaries (distinct from simulation command outputs that carry SimulationRun provenance), holding zone contents awaiting integration, reference documents reviewed during sessions, and exploratory analysis that informed decisions without becoming artifacts. This peripheral intelligence lives in an Annotation Layer: structurally present on the board, linked to Sessions and timestamps, but not committed to the Field Ledger unless explicitly promoted. The Annotation Layer is not a kernel object; it is a structural pattern that implementation-layer systems may formalize. The kernel requires only that the distinction between ledger-committed intelligence and annotation-layer intelligence be explicit and that promotion from annotation to ledger (committing peripheral intelligence as a formal artifact within an Exercise) is a deliberate act that passes through a commit gate. An annotation that is never promoted is preserved for reference but does not affect FieldState computation, dimension distribution, or any kernel-defined metric. This preserves the Field Ledger's integrity as a record of committed transformations while acknowledging that boards produce more intelligence than they formally commit.

**NAMED DIAGNOSTIC CONDITIONS:** The following conditions are recognized field health patterns derivable from FieldState metrics. They are named here to provide simulation engines and facilitators with a shared diagnostic vocabulary. These are not error states but structural conditions that may be healthy or unhealthy depending on context, consistent with the FieldState Interpretation Note above.

> **Dimensional Blindspot:** A scope consistently shows zero or near-zero activation in one or more dimensions across multiple Sessions, while adjacent dimensions are well-populated. Derivable from dim_distribution and shadow_distribution. Indicates that the intelligence field may be systematically unable to perceive or produce intelligence at the absent dimension. Distinct from intentional scoping (a zone with allowed_dimensions constraining to 2D–3D is not blindspotted, it is scoped). A blindspot is diagnosed when absence occurs *outside* structural constraints. Simulations encountering a blindspot SHOULD flag the absent dimension and evaluate whether shadow presence exists there (per Shadow Invariant 5, Section 4.2).
>
> **Dimensional Collapse:** A scope shows extreme concentration in a single dimension with corresponding depletion across all others, accompanied by high gravity on a narrow set of zones and rising fatigue. Derivable from dim_distribution, gravity_map, saturation, and fatigue. Indicates that intelligence has become trapped in a single mode of thinking, creating a self-reinforcing attractor that resists dimensional movement. Distinct from healthy concentration (early-stage boards may legitimately focus on 1D–2D). Collapse is diagnosed when concentration persists across multiple Sessions despite facilitation intent to broaden, and when fatigue confirms that recursive processes within the concentrated dimension are producing diminishing returns.
>
> **Bridge Erosion:** A scope shows stable or increasing Bridge density but Comparison data across Snapshots reveals that bridge rationales are becoming thinner, contradictory, or semantically repetitive indicating that connections are being maintained structurally but losing coherent justification. Derivable from bridge density counts in FieldState, rationale quality evaluation across Snapshot-scoped Comparisons, and correlation with rising curvature or fatigue in the bridged zones. Indicates that the intelligence field is preserving the *appearance* of connection (6D) without sustaining the *substance* of it. Distinct from low Bridge density (which may indicate early-stage development or intentional scoping). Bridge Erosion is diagnosed when connections exist but their semantic load is degrading over time, particularly under high curvature or fatigue conditions. Simulations encountering Bridge Erosion SHOULD evaluate whether the bridged zones have diverged dimensionally (making the original bridge rationale obsolete) or whether fatigue in the connecting dimension has shifted bridging activity from constructive (6D creative) to extractive (6D shadow) orientation.
>
> **Productive Polarity:** A scope shows sustained tension (tension_density > 0 across multiple Sessions) that correlates with increasing dimensional migration, new bridge formation, and rising field_resonance. The tension is generating movement: artifacts are shifting dimensions, new connections are forming, and the field's emergent intelligence is increasing. Derivable from tension_map, Comparison dimension_migrations[], bridge density trends, and field_resonance. Indicates that the intelligence field contains a generative opposition, where two or more perspectives cannot be trivially reconciled but their interaction produces insight neither could generate alone. Productive Polarity often clusters around the 5D threshold (competing identity definitions) and at 3D (competing contextual frameworks). Facilitation response: hold the tension. Do not rush resolution. The field is working.
>
> **Destructive Polarity:** A scope shows sustained tension that correlates with decreasing coherence, gravity draining from tensioned zones, rising fatigue, and bridge erosion in the areas connecting the opposing positions. The tension is fragmenting the field: participants are retreating to their positions, cross-boundary bridges are losing substance, and the field's intelligence is diminishing. Derivable from tension_map, coherence trend, gravity_map shifts, fatigue, and bridge erosion indicators. Indicates that the opposition has calcified into entrenchment. Destructive Polarity often reflects pillar misalignment at a fundamental level: the opposing positions are not just asserting different claims but operating from different pillar orientations (one Heart-led, the other Truth-led) without a Nuance bridge between them. Facilitation response: intervene. The field cannot resolve this without active facilitation, typically through the Map Tension Field simulation command (Section 7.2) to make the polarity structure visible, followed by targeted exercises that surface the pillar misalignment.
>
> **Arrested Development:** A board shows a sustained pattern of field activity (artifacts produced, sessions conducted, simulations run) without corresponding evolution. Dimensional positions are not changing, transitions are not completing, and the evolution_phase has been classified as "dormant" or has remained in "expansion" without ever entering "consolidation" for a duration exceeding three Sessions. Derivable from evolution_velocity, evolution_phase, transition_completions, and transition_stalls across Comparisons. Indicates that the field is metabolizing energy without producing structural growth. Distinct from intentional dormancy (a board placed on hold) and from Dimensional Collapse (which shows concentration, not stasis). Arrested Development is diagnosed when the facilitation intent is active development but the field metrics show no movement. Common causes include: prompt dimensionality too low for the board's current state, unresolved tension that blocks forward movement (see Destructive Polarity), and facilitator avoidance of shadow dimensions. Simulations encountering Arrested Development SHOULD evaluate these three factors — prompt dimensionality mismatch, tension blockage, and shadow avoidance — as part of the diagnostic.

**EMBODIMENT SIGNAL NOTE:** DN-compliant systems process two qualitatively different modes of engagement: mechanical application and dimensional embodiment. Both produce valid, spec-compliant outputs. The difference is observable in FieldState patterns across Sessions. Mechanical application tends to produce: artifacts tagged at prescribed dimensions matching zone allowed_dimensions, pillar_lead consistently matching zone pillar_affinity, bridges confined within section boundaries, zero or minimal shadow presence, low resonant_transformation counts in Comparisons, and stable but flat gravity maps with no unexpected concentration. Dimensional embodiment tends to produce: artifacts that land at dimensions the zone did not prescribe but the field structurally required, bridges crossing section and zone boundaries revealing unanticipated connections, conscious shadow engagement, resonant transformations detected between snapshots, Story Thread formation across multiple dimensions, and gravity that concentrates in ways the template did not predict. Neither mode is an error. Mechanical application may be appropriate for early-stage boards or structured training contexts. But simulation engines evaluating field health SHOULD recognize that a board exhibiting only mechanical-application patterns may be spec-compliant without being dimensionally alive, and that the absence of surprise, emergence, and cross-boundary connection in a mature board is itself a diagnostic signal.

---

## 7. Simulation Contracts

Each simulation command in the 5D Prompt Singularity system is defined here as a typed contract: what it accepts, what it produces, and what constraints govern its execution. These contracts turn prose descriptions into implementable interfaces.

### 7.1 Primary Simulation Commands

**Ignite Reality Rift**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Simulate potential strategic outcomes. Identify opportunity gaps and dimensional misalignments. Generate 'what if' scenarios. |
| **Input** | scope_ids[] (artifacts to analyze), scenario_type (optional: Market Shock, etc.), context (optional freetext) |
| **Output** | scenarios[] (each with: narrative, artifacts_affected[], dimension_shifts[], risk_level), pillar_balance, field_state_delta |
| **Constraint** | Must evaluate both creative and shadow orientations of each scenario. Must tag pillar_lead per scenario. |

**Forge Love Bridge**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Create connections between disparate elements. Identify resonance points. Map dimensional pathways for cross-domain integration. |
| **Input** | source_ids[] (artifacts/zones to connect from), target_ids[] (artifacts/zones to connect to), bridge_type (optional) |
| **Output** | bridges[] (each with: source, target, rationale, resonance_score, dimension_pathway[]), pillar_balance |
| **Constraint** | Use when connection is unclear, not when imbalance is the issue. Must produce Bridge objects with semantic rationale. |

**Usher Golden Age**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Project forward evolution. Simulate ideal execution and response. Map path from current state to goal state. |
| **Input** | scope_ids[], mode (Vision | Milestone), time_horizon (optional), goal_state (optional description) |
| **Output** | projection (narrative), milestones[] (if Milestone mode, each with: dimension, artifacts, timeline), transitions[], pillar_balance |
| **Constraint** | Use when goal state is known but path isn't. Must produce traceable transition chain. |

**Weave Dimensional Thread**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Run a cross-section storyline across all dimensions 1D–9D. Full-spectrum narrative trace. |
| **Input** | subject (project/product/brand name), scope_ids[] (optional, for grounding in existing artifacts) |
| **Output** | thread[] (one entry per dimension: {dimension, narrative_beat, artifacts_referenced[], shadow_note}), pillar_balance |
| **Constraint** | Must include shadow_note for each dimension. Must identify the Singularity Point (5D lock). |

**Create Storyfield**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Narrate how ideas or organizations move through the dimensional model as arcs of becoming. |
| **Input** | subject (entity name), scope_ids[] (optional) |
| **Output** | storyfield_trace[] (one per dimension: {dimension, narrative, signal_lock: boolean}), missed_bridges[], echoing_dimension, pillar_balance |
| **Constraint** | Must identify: Singularity Point, missed Bridges, and which dimension 'still echoes.' |

### 7.2 Supplemental Commands

**Run Dimensional Audit**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Analyze scope for balanced dimensional coverage. Identify over- and under-represented dimensions. |
| **Input** | scope_ids[] (board, section, or zone), audit_type (full | section_only) |
| **Output** | dim_distribution, shadow_distribution, gaps[], recommendations[], field_state |
| **Constraint** | MUST report shadow presence/absence. Use as first diagnostic step before any simulation. |

**Initiate Gravity Mapping**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Map how resources, attention, and energy flow through the scope. |
| **Input** | scope_ids[], mapping_mode (standard | vector | layered) |
| **Output** | gravity_map (zone_id → score), pillar_vectors (if vector mode), internal_vs_external (if layered mode), recommendations[] |
| **Constraint** | Pairs naturally with Dimensional Audit. Must suggest resource allocation for optimal impact. |

**Spark Fire Test**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Stress-test strategic elements. Identify what strengthens and what collapses under pressure. |
| **Input** | scope_ids[], test_mode (domain-specific; e.g., Market Shock, Team Friction, Scaling Pressure — defined by Template) |
| **Output** | results[] (per artifact: {survived: boolean, strengthened: boolean, shadow_exposed: boolean, refinement_path}), fragility_map, pillar_balance |
| **Constraint** | MUST evaluate both creative and shadow orientations. Must produce fragility map and survivability assessment. |

**Explore Shadow Symmetry**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Generate shadow-orientation counterparts to creative-layer artifacts. Surface probable opposing risks, blindspots, and destructive recursion patterns that the creative layer implies but does not articulate. |
| **Input** | scope_ids[] (artifacts to analyze), depth (singular | scenario), scenario_count (integer, required if depth: scenario, default: 3) |
| **Output** | shadow_artifacts[] (each with: source_artifact_id, content, dimension { primary, shadow: true, nested }, pillar_lead, scenario_label (null if depth: singular)), shadow_bridges[] (connecting each shadow artifact to its source), pillar_balance |
| **Constraint** | Every output artifact MUST carry dimension.shadow: true. shadow_bridges[] MUST link each generated artifact to its creative-layer source via bridge_type: "shadow_symmetry". When depth: scenario, each scenario_label must describe the distinct risk vector explored. Must tag pillar_lead per shadow artifact. |

**Reveal Resonance Field**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Evaluate the retroactive significance shift across board artifacts following a 5D+ recognition event. Identifies artifacts whose operational meaning has transformed due to higher-dimensional activation; not artifacts that moved dimensions, but artifacts that now carry different weight, relevance, or structural importance within the field. |
| **Input** | trigger_artifact_ids[] (the 5D+ artifact(s) that achieved recognition or Signal Lock), scope_ids[] (board, section, or zone to evaluate — defaults to full board), recognition_type (signal_lock | dimensional_arrival | identity_definition) |
| **Output** | resonant_candidates[] (each with: artifact_id, current_dimension, transformation_signal, significance_shift (elevated | diminished | recontextualized), pillar_lead), pillar_balance |
| **Constraint** | MUST only be invoked after a 5D+ recognition event has been established. The trigger artifact(s) must be at dimension 5 or higher. Output artifacts are NOT re-tagged — their dimensional position is unchanged. The command evaluates meaning-shift-in-place per Constraint 5 (Resonant Activation, Section 2.1). Must tag pillar_lead per candidate. Pairs naturally with Resonance Result as a close, and its output feeds directly into resonant_transformations[] in the next Comparison (Section 8.9). |

**Generate Resonance Result**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Wrap any simulation with a summary of what shifted or clarified. The universal debrief command. |
| **Input** | simulation_run_id (references a completed SimulationRun) |
| **Output** | resonance_summary, signal_locks[] (ideas that achieved Signal Lock), cross_links[] (to other board sections), pillar_balance |
| **Constraint** | Must note if Signal Lock was achieved on any specific idea. Must cross-reference board sections. |

**Map Tension Field**

| **Contract Field** | **Specification** |
|---|---|
| **Purpose** | Identify, measure, and characterize field tension within a scope. Surface artifact pairs with opposing claims, diagnose the pillar and dimensional structure of each opposition, and produce a polarity map that reveals where the field's energy is concentrated in conflict versus alignment. When opposing 5D+ recognitions exist, analyze the space between them to generate a narrative of what each position sees that the other cannot. |
| **Input** | scope_ids[] (board, section, or zone to evaluate), depth (scan \| diagnostic \| narrative), focal_artifacts[] (optional: specific artifacts suspected of being in tension; when two opposing 5D+ artifacts are provided, the command performs deep narrative analysis of the space between them) |
| **Output** | tension_pairs[] (each with: artifact_id_a, artifact_id_b, dimension, polarity_score, pillar_divergence, narrative), polarity_map (visual/structural representation of attraction and repulsion across the scope), synthesis_candidates[] (artifact pairs whose tension appears resolvable at a higher dimension, e.g., two competing 3D contexts that a 5D identity could transcend), pillar_balance |
| **Constraint** | Must distinguish between creative and destructive tension per the Named Diagnostic Conditions (Section 6). When focal_artifacts include opposing 5D+ recognitions, MUST produce a narrative analyzing what each recognition illuminates and what it obscures, identifying the structural gap between them and whether a higher-dimensional synthesis (6D bridge, 7D manifestation, or 8D recursive integration) could encompass both. Must tag pillar_lead per tension pair. Output feeds directly into FieldState tension_map computation. |

### 7.3 Simulation Routing

The simulation contracts in Sections 7.1 and 7.2 define what each command does. This section defines when to use which command. DN-compliant systems that expose simulation capabilities SHOULD implement this routing logic to select the appropriate command for a given field condition. The routing is not exclusive as multiple commands may apply, and sequencing matters.

| **Field Condition** | **Recommended Command(s)** | **Reasoning** |
|---|---|---|
| High ambiguity, many artifacts, no clarity | Run Dimensional Audit → Initiate Gravity Mapping | Diagnose what's overemphasized and where energy flows before intervening. These two commands pair as the standard opening diagnostic. |
| Strategic fork, multiple viable paths | Ignite Reality Rift | Explore diverging futures from the current state. Use when the decision is which path, not what's wrong. |
| Disconnected sections, fragmented intelligence | Forge Love Bridge | Merge disconnected elements by surfacing resonance. Use when connection is unclear, not when imbalance is the issue. |
| Known goal state, unknown path | Usher Golden Age | Backcast milestones from ideal future. Use when destination is defined but the transition chain isn't. |
| Perceived vulnerability, untested assumptions | Spark Fire Test | Simulate fragility under stress. Produces survivability assessment and refinement paths. |
| Need to translate vision into narrative | Weave Dimensional Thread | Build cross-dimensional coherence from 1D through 9D as a single storyline. |
| Need to understand how thinking evolved | Create Storyfield | Map the dimensional journey of an idea or identity, including missed transitions and emergence points. |
| Creative-layer artifacts need shadow examination | Explore Shadow Symmetry | Generate shadow counterparts to surface blindspots, risks, and destructive recursion patterns the creative layer implies but doesn't articulate. |
| 5D+ recognition achieved, need to understand downstream impact | Reveal Resonance Field | Evaluate which existing artifacts carry new weight or significance following a defining recognition. Use when a Signal Lock or identity definition has just landed and the field needs re-reading through that new lens. |
| Any simulation completed | Generate Resonance Result | Universal debrief. Wraps any simulation with a summary of what shifted or clarified. Always available as a closing command. |
| Competing claims at same dimension, declining coherence | Map Tension Field → Forge Love Bridge | Diagnose the polarity structure before attempting connection. The tension must be named before it can be bridged. |
| Opposing 5D+ recognitions, participants entrenched | Map Tension Field (with focal_artifacts) → Reveal Resonance Field | Map what each recognition sees, then evaluate how existing artifacts carry different weight under each perspective. The space between opposing identities often contains the field's deepest intelligence. |

**ROUTING PRINCIPLE:** Dimensional Audit is the recommended first diagnostic step before any other simulation. When field conditions are unclear, begin with Audit → Gravity Mapping to establish baseline understanding before selecting a targeted simulation command.

**SEQUENCING PRINCIPLE:** Simulation outputs may feed subsequent simulations. Common sequences include: Run Dimensional Audit → Initiate Gravity Mapping (diagnostic pair), Ignite Reality Rift → Weave Dimensional Thread (scenario exploration → narrative synthesis), Usher Golden Age → Create Storyfield (goal projection → evolutionary arc), Spark Fire Test → Explore Shadow Symmetry (stress test → shadow depth analysis), Reveal Resonance Field → Generate Resonance Result (recognition impact → summary debrief), Map Tension Field → Forge Love Bridge (polarity diagnosis → connection attempt), Map Tension Field → Reveal Resonance Field (opposing recognitions → differential resonance analysis), and any command → Generate Resonance Result (universal close). Simulation chaining is not required but is recognized as a pattern that produces richer intelligence than isolated command execution.

---

## 8. Serialization Format

This section defines the JSON schema essentials for serializing DN objects. This is the contract that makes board exports self-documenting and enables any receiving system to interpret DN-structured data without loading the full corpus.

### 8.1 Artifact Schema

The minimum viable JSON representation of a DN artifact:

```json
{
  "id": "art_001",
  "content": "Our customers fear irrelevance more than failure",
  "dimension": {
    "primary": 3,
    "shadow": false,
    "nested": null
  },
  "pillar_lead": "nuance",
  "pillar_stabilizers": ["heart", "truth"],
  "exercise_id": "ex_001",
  "source_type": "simulation",
  "simulation_run_id": null,
  "import_batch_id": "batch_001",
  "branch_id": null,
  "created_at": "2026-02-13T00:00:00Z",
  "metadata": {
    "source": "workshop_session_1",
    "confidence": 0.85
  }
}
```

**New fields:** source_type is always required per Section 1.2 and identifies the signal origin (conscious | ambient | environmental | simulation). A human-created artifact carries source_type: "conscious". simulation_run_id references internal SimulationRun (Section 1.4). import_batch_id references Provenance Group (Section 1.3). branch_id scopes to a Branch (Section 1.1). These three are nullable; a human-created artifact on the main timeline carries null for all three.

### 8.2 Board Export Schema

A board export includes the full hierarchy plus embedded semantic context. The following example uses the Growth Blueprint Template for illustration; the schema is domain-universal.

```json
{
  "board": {
    "id": "board_001",
    "name": "Acme Corp Growth Blueprint",
    "template_id": "tmpl_growth_blueprint",
    "workspace_id": "ws_001",
    "field_state": {
      "scope_id": "board_001",
      "coherence": 0.0,
      "drift": 0.0,
      "saturation": 0.0,
      "fatigue": 0.0,
      "dim_distribution": {"1D": 0, "2D": 0, "3D": 0, "4D": 0, "5D": 0, "6D": 0, "7D": 0, "8D": 0, "9D": 0},
      "shadow_distribution": {"1D": 0, "2D": 0, "3D": 0, "4D": 0, "5D": 0, "6D": 0, "7D": 0, "8D": 0, "9D": 0},
      "pillar_balance": {"heart": 0, "truth": 0, "nuance": 0},
      "curvature": {"heart": 0.0, "truth": 0.0, "nuance": 0.0, "composite": 0.0},
      "tension_density": 0.0,
      "evolution_velocity": 0.0,
      "evolution_phase": "expansion",
      "computed_at": "2026-02-16T00:00:00Z"
    },
    "created_at": "2026-01-15T00:00:00Z",
    "updated_at": "2026-02-16T00:00:00Z",
    "sections": [{
      "id": "sec_01",
      "name": "Customer Profile",
      "purpose": "Map the customer's world",
      "order": 1,
      "zones": [{
        "id": "zone_goals_&_priorities",
        "name": "Company Goals",
        "prompt": "What do we want to achieve?",
        "allowed_dimensions": [2, 3],
        "dimension_rules": {
          "2D": "Validated data points",
          "3D": "Contextual patterns"
        },
        "simulation_rules": {},
        "exercises": [{
          "id": "ex_001",
          "name": "Goal Identification",
          "purpose": "Identify primary business objectives",
          "methodology": "Brainstorm and prioritize",
          "component_parts": [],
          "output_format": "artifact_list",
          "key_linkages": [],
          "order": 1,
          "prerequisites": [],
          "dimension_affinity": 2,
          "pillar_affinity": "truth",
          "artifacts": [ /* Artifact objects per 8.1 schema */ ]
        }]
      }]
    }]
  },
  "kernel_version": "0.9",
  "shadow_kernel": true,
  "pillar_metric": true,
  "color_system": {
    "1D": "#E84C88",
    "2D": "#3A86C8",
    "3D": "#7B5EA7",
    "4D": "#7B5EA7",
    "5D": "#2D8B46",
    "6D": "#E87C2E",
    "7D": "#D4A017",
    "8D": "#1A9E96",
    "9D": "#1A1A2E",
    "shadow": "#8B0000",
    "urgent": "#DC143C"
  }
}
```

**color_system note:** The "shadow" entry (#8B0000) is an overlay modifier, not a standalone dimension color. Shadow-tagged artifacts retain their dimensional color (e.g., a 3D shadow artifact is still Violet) with the shadow color applied as a visual differentiator — typically a border, outline, or background tint. This preserves dimensional readability while surfacing shadow orientation. The "urgent" entry (#DC143C) follows the same modifier pattern. Neither replaces a dimensional color; both layer on top of one.

### 8.3 Extraction Rule

**DETERMINISTIC RULE:** When extracting from a Template's source documentation for board-embedded context, include ONLY sections that define machine-interpretable rules for each zone (zone names, zone prompts, dimension constraints, exercise instructions with structured outputs). Everything else (facilitation narrative, meeting guidance, philosophical framing) belongs to the corpus layer (Section 9.1) and is not embedded in the board schema. This rule is keyed to the board JSON schema. If a section does not map to a schema field, it is not extracted.

### 8.4 Branch Schema

The minimum viable JSON representation of a DN Branch:

```json
{
  "id": "branch_001",
  "board_id": "board_001",
  "name": "What if we led with enterprise?",
  "fork_snapshot_id": "snap_003",
  "parent_branch_id": null,
  "status": "active",
  "created_at": "2026-02-15T00:00:00Z",
  "metadata": {
    "fork_rationale": "Exploring enterprise-first GTM as alternative",
    "pillar_lead": "truth"
  }
}
```

**Required fields:** id, board_id, name, fork_snapshot_id, status. parent_branch_id is null for branches from the main timeline; non-null for branches forked from other branches.

### 8.5 ImportBatch (Provenance Group) Schema

The minimum viable JSON representation of a DN Provenance Group:

```json
{
  "id": "batch_001",
  "session_id": "session_007",
  "source_description": "Claude conversation: client goal mapping",
  "artifact_ids": ["art_041", "art_042", "art_043", "art_044"],
  "timestamp": "2026-02-15T14:30:00Z",
  "import_metadata": {
    "source_tool": "claude.ai",
    "zones_affected": ["zone_goals_&_priorities", "zone_market_risks"],
    "artifact_count": 4
  }
}
```

### 8.6 Exercise Schema

The minimum viable JSON representation of a DN Exercise:

```json
{
  "id": "ex_001",
  "zone_id": "zone_goals_&_priorities",
  "name": "Goal Identification",
  "purpose": "Identify and articulate primary business objectives",
  "methodology": "Guided brainstorm with prioritization ranking",
  "component_parts": [
    "Individual brainstorm",
    "Group synthesis",
    "Priority ranking"
  ],
  "output_format": "artifact_list",
  "key_linkages": [
    {
      "target_id": "ex_002",
      "type": "informs"
    }
  ],
  "order": 1,
  "prerequisites": [],
  "dimension_affinity": 2,
  "prompt_dimension": 2,
  "pillar_affinity": "truth",
  "completion_criteria": {
    "checklist": [
      "Core objectives stated in ≤ 15 words each",
      "Named beneficiary or stakeholder per objective",
      "No contradiction with existing core values",
      "Review date set"
    ]
  },
  "artifacts": [ /* Artifact objects per 8.1 schema */ ]
}
```

**Required fields:** id, zone_id, name, purpose, methodology, component_parts[], output_format, key_linkages[], order, prerequisites[], dimension_affinity, pillar_affinity. prompt_dimension is nullable; when populated, it records the structural dimension at which the Exercise's prompt activates intelligence (Section 2.4). A prompt_dimension lower than dimension_affinity indicates the prompt structurally constrains output below the Exercise's intended dimensional target. This mismatch is diagnostic signal: the Exercise asks for intelligence at one level but activates it at another. completion_criteria is nullable; when populated, it defines the verifiable conditions that must be true for this Exercise's work to count as complete (Section 1.6, Completion Criteria). key_linkages[] entries carry a target_id and a type (dependency | informs | follows_up) per Table 1. artifacts[] contains the Exercise's produced Artifacts serialized per Section 8.1.

### 8.7 Bridge Schema

The minimum viable JSON representation of a DN Bridge:

```json
{
  "id": "bridge_001",
  "source_id": "art_001",
  "target_id": "art_027",
  "bridge_type": "resonance",
  "rationale": "Customer fear of irrelevance directly feeds competitive positioning urgency",
  "dimension": {
    "primary": 6,
    "shadow": false,
    "nested": null
  },
  "scope": "intra-board"
}
```

**Required fields:** id, source_id, target_id, bridge_type, rationale, dimension, scope. source_id and target_id may reference Artifacts, Exercises, Zones, Sections, or Boards per Section 1.1 — Bridges may cross all containment boundaries. bridge_type is implementation-defined (e.g., resonance, tension, dependency, translation). rationale is required and must provide semantic justification for why the connection exists — Bridges without rationale are spec violations. scope is intra-board (default, both endpoints within the same Board) or cross-board (endpoints in different Boards within the same Workspace; see Section 8.12).

### 8.8 Snapshot Schema

The minimum viable JSON representation of a DN Snapshot:

```json
{
  "id": "snap_003",
  "board_id": "board_001",
  "inflection_label": "Post-discovery session: customer fears validated",
  "timestamp": "2026-02-10T16:00:00Z",
  "field_state": { /* computed FieldState per Section 6.1 */ },
  "artifact_states": [
    {
      "artifact_id": "art_001",
      "dimension": {
        "primary": 3,
        "shadow": false,
        "nested": null
      },
      "pillar_lead": "nuance",
      "pillar_stabilizers": ["heart", "truth"]
    }
  ]
}
```

**Required fields:** id, board_id, inflection_label, timestamp, field_state, artifact_states[]. inflection_label is a human-authored description of why this moment warranted a snapshot — it is not auto-generated. artifact_states[] captures each artifact's dimensional position and pillar lead at the moment of the snapshot, enabling precise delta computation in Comparisons. The full artifact content is not duplicated — artifact_states[] records positional coordinates only, referencing artifacts by id.

### 8.9 Comparison Schema

The minimum viable JSON representation of a DN Comparison:

```json
{
  "id": "comp_001",
  "snapshot_ids": ["snap_001", "snap_003"],
  "scope": "intra-board",
  "delta_field_state": {
    "coherence_delta": 0.15,
    "drift_delta": -0.08,
    "saturation_delta": 0.22,
    "fatigue_delta": 0.03
  },
  "dimension_migrations": [
    {
      "artifact_id": "art_001",
      "from_dimension": {
        "primary": 2,
        "shadow": false
      },
      "to_dimension": {
        "primary": 3,
        "shadow": false
      }
    }
  ],
  "resonant_transformations": [
    {
      "artifact_id": "art_005",
      "dimension": 2,
      "trigger_dimension": 5,
      "trigger_artifact_id": "art_019",
      "transformation_signal": "Market validation data recontextualized as identity-confirming evidence after strategic positioning lock"
    }
  ],
  "gravity_shifts": [
    {
      "zone_id": "zone_goals_&_priorities",
      "from_score": 0.6,
      "to_score": 0.85
    }
  ],
  "shadow_emergence": [
    {
      "artifact_id": "art_012",
      "dimension": 5,
      "signal": "Recognition oriented toward isolation rather than connection"
    }
  ],
  "transition_completions": ["trans_004", "trans_007"],
  "transition_stalls": ["trans_002"]
}
```

**Required fields:** id, snapshot_ids[], scope, delta_field_state, dimension_migrations[], resonant_transformations[], gravity_shifts[], shadow_emergence[], transition_completions[], transition_stalls[]. scope is intra-board (default, all Snapshots from the same Board) or cross-board (Snapshots drawn from different Boards within the same Workspace; see Section 8.12). snapshot_ids[] must contain two or more Snapshot ids per Section 1.1. delta_field_state captures the change in FieldState metrics between the earliest and latest snapshots; for cross-board Comparisons, delta_field_state captures the structural differences between the two Boards' FieldStates at their respective snapshot moments. dimension_migrations[] records every artifact that changed dimensional position between snapshots. resonant_transformations[] records artifacts whose operational significance changed due to higher-dimensional activation without changing their own dimensional position (Constraint 5). Each entry identifies the artifact, its stable dimension, the higher dimension whose activation triggered the transformation, the triggering artifact, and a signal describing how the meaning shifted. gravity_shifts[] records zones whose gravity scores changed. shadow_emergence[] surfaces artifacts that shifted to or exhibited shadow orientation. transition_completions[] and transition_stalls[] reference Transition ids that completed or stalled during the comparison window.

### 8.10 Session Schema

The minimum viable JSON representation of a DN Session:

```json
{
  "id": "session_007",
  "board_id": "board_001",
  "intent_class": "refinement",
  "timestamp_start": "2026-02-15T09:00:00Z",
  "timestamp_end": "2026-02-15T12:30:00Z",
  "participants": [
    {
      "type": "human",
      "role": "facilitator",
      "identity": "lead_facilitator_01",
      "dimensional_affinity": [3, 5, 6],
      "dimensional_actual": [3, 4, 5]
    },
    {
      "type": "ai",
      "role": "contributor",
      "identity": "simulation_engine_01",
      "dimensional_affinity": [2, 3, 6],
      "dimensional_actual": [2, 3, 5, 6]
    }
  ],
  "environmental_signals": {
    "setting": "virtual",
    "platform": "blueprint_board",
    "session_duration_minutes": 210
  },
  "simulation_parameters": {
    "routing_mode": "standard",
    "shadow_depth": "enabled"
  },
  "change_rationale": "Post-review session: participant feedback revealed a gap between contextual mapping and identity formation. Revisiting 4D exercises to ground the emerging 5D recognition.",
  "completion_criteria": [
    {
      "id": "dod_001",
      "name": "Define & Coherence",
      "dimension_focus": 5,
      "checklist": [
        "Essence stated in one sentence",
        "Contradictions with other cores resolved",
        "Stakeholder recognition signals defined",
        "Artifact representing identity created and linked",
        "Review trigger defined"
      ],
      "status": "met"
    }
  ],
  "artifacts_produced": ["art_041", "art_042", "art_043", "art_044"],
  "transitions_recorded": ["trans_008", "trans_009"],
  "snapshot_id": "snap_004"
}
```

**Required fields:** id, board_id, intent_class, timestamp_start, timestamp_end, participants[], environmental_signals{}, simulation_parameters{}, change_rationale, artifacts_produced[], transitions_recorded[]. completion_criteria[] is recommended but nullable; when present, each entry carries an id, name, dimension_focus, checklist (array of verifiable conditions), and status (pending | met | unmet, evaluated at session close). Completion criteria are established at session start and evaluated at session close; they formalize what "done" means for this session's work (Section 1.6, Completion Criteria). snapshot_id is nullable; populated only when a Snapshot is triggered on session close. Each participant entry carries type (human | ai), role (facilitator | contributor | observer), identity, dimensional_affinity[] (expected operating dimensions, set at session start), and dimensional_actual[] (computed from artifacts_produced, populated on session close). change_rationale is human-authored and captures the intent and context for the session; it is the primary narrative thread consumed by Evolution Tracking (Section 1.1.1).

### 8.11 Template Schema

The minimum viable JSON representation of a DN Template:

```json
{
  "id": "tmpl_growth_blueprint",
  "name": "Growth Blueprint",
  "description": "A structured intelligence field for mapping organizational growth across all nine dimensions.",
  "sections": [
    {
      "id": "sec_01",
      "name": "Customer Profile",
      "purpose": "Map the customer's world",
      "order": 1,
      "zones": [
        {
          "id": "zone_goals_&_priorities",
          "name": "Company Goals",
          "prompt": "What do we want to achieve?",
          "allowed_dimensions": [2, 3],
          "dimension_rules": {
            "2D": "Validated data points",
            "3D": "Contextual patterns"
          },
          "simulation_rules": {},
          "exercises": [
            {
              "id": "ex_001",
              "name": "Goal Identification",
              "prompt": "Identify and articulate the primary objectives driving this initiative.",
              "dimension_affinity": 2,
              "pillar_affinity": "truth",
              "order": 1,
              "prerequisites": []
            }
          ]
        }
      ]
    }
  ],
  "allowed_dimensions": [1, 2, 3, 4, 5, 6, 7, 8, 9],
  "dimension_rules": {
    "5D": "Requires evidence of 1D-4D traversal before Signal Lock candidacy"
  },
  "simulation_rules": "Standard routing per Section 7.3",
  "exercise_order": "sequential_within_zone",
  "prerequisites": []
}
```

**Required fields:** id, name, description, sections[] (each containing zones[], and each zone containing exercises[] with prompts, allowed_dimensions[], dimension_rules{}, and simulation_rules), allowed_dimensions[], dimension_rules{}, simulation_rules, exercise_order, prerequisites[]. sections[] defines the Template's structural hierarchy; zones within sections carry their own allowed_dimensions[] and dimension_rules{} that may narrow (but not broaden) the Template-level dimensional scope. exercises[] within zones carry prompts, dimension_affinity, pillar_affinity, ordering, and prerequisites that define the unit of work. exercise_order governs how exercises sequence within zones (e.g., sequential, parallel, facilitator-directed). prerequisites[] at the Template level define any preconditions for Template instantiation. A Board is created by instantiating a Template; the Template's structure becomes the Board's initial configuration.

### 8.12 Workspace Schema

The minimum viable JSON representation of a DN Workspace:

```json
{
  "id": "ws_001",
  "name": "Pet Food M&A Portfolio",
  "description": "Assessment workspace for evaluating acquisition targets against strategic fit criteria.",
  "board_ids": ["board_001", "board_002", "board_003"],
  "cross_board_bridges": [
    {
      "id": "bridge_xb_001",
      "source_id": "art_board001_052",
      "target_id": "art_board002_018",
      "bridge_type": "resonance",
      "rationale": "Both companies identify premium nutrition positioning as core 5D identity.",
      "dimension": { "primary": 5, "shadow": false, "nested": null },
      "scope": "cross-board"
    },
    {
      "id": "bridge_xb_002",
      "source_id": "art_board001_031",
      "target_id": "art_board003_044",
      "bridge_type": "tension",
      "rationale": "Competing distribution strategies: direct-to-consumer vs. retail-first.",
      "dimension": { "primary": 3, "shadow": false, "nested": null },
      "scope": "cross-board"
    }
  ],
  "workspace_field_state": {
    "board_count": 3,
    "boundary_permeability": { "board_001-board_002": 0.72, "board_001-board_003": 0.31, "board_002-board_003": 0.45 },
    "dimensional_alignment": {
      "board_001-board_002": { "1D": 0.8, "2D": 0.6, "3D": 0.4, "4D": 0.2, "5D": 0.9, "6D": 0.5, "7D": 0.3, "8D": 0.1, "9D": 0.0 },
      "board_001-board_003": { "1D": 0.3, "2D": 0.7, "3D": -0.6, "4D": 0.4, "5D": -0.2, "6D": 0.1, "7D": 0.5, "8D": 0.0, "9D": 0.0 },
      "board_002-board_003": { "1D": 0.5, "2D": 0.5, "3D": -0.3, "4D": 0.3, "5D": 0.1, "6D": 0.4, "7D": 0.2, "8D": 0.0, "9D": 0.0 }
    },
    "phase_compatibility": { "board_001-board_002": "compatible", "board_001-board_003": "divergent", "board_002-board_003": "neutral" },
    "cross_board_bridge_count": 2,
    "cross_board_tension_density": 0.5,
    "computed_at": "2026-02-22T10:00:00Z"
  },
  "created_at": "2026-02-01T00:00:00Z",
  "updated_at": "2026-02-22T10:00:00Z"
}
```

**Required fields:** id, name, description, board_ids[], cross_board_bridges[], workspace_field_state, created_at, updated_at. board_ids[] references all Boards belonging to this Workspace. cross_board_bridges[] contains Bridge objects with scope: cross-board, connecting artifacts or structural elements across different Boards in the Workspace. workspace_field_state is the inter-field FieldState computed across all constituent Boards, containing: pairwise boundary_permeability (Section 10.3), pairwise dimensional_alignment (Section 10.3), pairwise phase_compatibility (Section 10.3), cross_board_bridge_count, cross_board_tension_density, and computed_at timestamp. The workspace_field_state is recomputed when any constituent Board's FieldState changes or when cross-board Bridges are created or modified. Cross-board Comparisons (Comparison objects with scope: cross-board) are produced by selecting Snapshots from different Boards within the Workspace and analyzing the delta between them; they follow the standard Comparison schema (Section 8.9) with the scope field distinguishing them from intra-board Comparisons.

---

## 9. Implementation Notes

### 9.1 Layer Architecture Reference

A DN-compliant system operates across three distinct layers. Each layer has a different purpose, a different audience, and a different relationship to this kernel.

| **Layer** | **Purpose** | **Contains** | **Relationship to Kernel** |
|---|---|---|---|
| **Kernel** | Defines what must be true. The structural constitution. | This document: Core Objects (Section 1), Dimensional Tags (Section 2), Pillar Metric (Section 3), Shadow Symmetry (Section 4), Transition Model (Section 5), Field Health Metrics (Section 6), Simulation Contracts (Section 7), Serialization Schemas (Section 8), Field-to-Field Dynamics (Section 10). | IS the kernel. Every structural requirement, constraint, invariant, and contract lives here. |
| **Corpus** | Explains why these structures exist. The philosophical and narrative foundation. | Standalone documents: Geometry of Intelligence, DN Code, Shadow Dimensions (full essay), Story Threads, Harmonies, Embodiment vs Application, RIP Triad (full narrative), and other framework texts that provide depth, context, and meaning behind the kernel's structural decisions. | INFORMS the kernel. The corpus provides the "why" that the kernel distills into "what." Corpus documents are never required at runtime; they support understanding, training, and facilitation depth. |
| **Implementation** | Determines how the structures are built. The product and platform layer. | Database schemas, API endpoints, UI components, authentication, hosting, AI integration, color systems, visual design, template authoring tools, and all platform-specific decisions. Includes the Growth Blueprint and other Templates as configured instances of the kernel's Template object. | IMPLEMENTS the kernel. Every implementation decision must respect kernel constraints but is free to make its own choices about technology, interface, and user experience. The kernel does not prescribe how to build; it prescribes what must be true about whatever is built. |

**LAYER BOUNDARY PRINCIPLE:** When a question arises during implementation, the layers resolve it in order. "What must this system do?" is answered by the kernel. "Why does it do this?" is answered by the corpus. "How should we build it?" is answered by the implementation layer. Confusion between layers (treating corpus narrative as structural requirement, or treating implementation choices as kernel constraints) is the most common source of architectural drift.

**AI CONTEXT NOTE:** When initializing an AI session for DN-structured work, the kernel and the Glossary together provide the structural and definitional foundation. Corpus documents may be added for depth when the session requires philosophical grounding, facilitation narrative, or domain-specific context. The kernel is always loaded; corpus documents are loaded as needed based on session intent. Templates are loaded when working within a specific Board's structure.

### 9.2 Kernel as Source of Truth

For any implementation (Blueprint Board, Replit build, future substrate), this Kernel is the source of truth for structural requirements. The full corpus provides depth, narrative, and philosophy. The spec provides contracts and constraints. When in doubt: if the question is 'what must this system do?' consult the spec. If the question is 'why does it do this?' consult the corpus.

### 9.3 Recursion Clause

This spec is itself subject to DN recursion (8D). Future versions will refine these definitions based on implementation experience, simulation testing, and field observation. Changes must pass through the Pillar Metric: Heart (does this honor the framework's soul?), Truth (is this structurally sound?), Nuance (does this respect contextual complexity?). Version changes are Transitions and must be documented as such.

---

## 10. Field-to-Field Dynamics

Axiom 8 (Section 0.3) establishes that every sustained interaction between intelligences generates a Unified Intelligence Field. The kernel defines the internal architecture of these fields: how they organize (Sections 1–2), how their quality is measured (Section 3), how their shadow operates (Section 4), how they evolve (Section 5), how their health is assessed (Section 6), and how they are operated upon (Section 7). But fields do not exist in isolation. Participants are themselves fields entering a board's field. Organizations run multiple boards whose fields overlap. The dimensional architecture describes intelligence at every scale, and at every scale, fields interact with other fields.

This section formalizes the initial structural model for field-to-field interaction. It is deliberately foundational, a prototype layer that future versions will refine through recursive application of the architecture to itself (per Section 9.3). The claim is not that this section captures the full complexity of field interaction, but that the rules governing how fields meet, influence, and transform each other are already implicit in the dimensional structure and can be made explicit.

### 10.1 Field Interaction Principle

Fields interact through the same mechanisms that operate within fields. A Bridge between two artifacts on the same board and a Bridge between two artifacts on different boards are the same structural object; the only difference is scope. A Transition within a single field and a Transition catalyzed by exposure to another field follow the same model; the only difference is the source of the catalyzing signal. The dimensional architecture does not change at the boundary between fields. What changes is the complexity of the interaction: within a field, all artifacts share a common FieldState context; between fields, each artifact carries the FieldState of its home field, and the interaction must negotiate between different states.

**FIELD INTERACTION INVARIANT:** The dimensional structure (1D–9D), pillar metric, shadow architecture, transition model, and all kernel constraints apply identically within and between fields. No special rules govern inter-field dynamics that do not also govern intra-field dynamics. The additional complexity is contextual (different FieldStates meeting), not structural (different rules applying).

### 10.2 Field Interaction Types

Fields interact across a spectrum of depth, from transient contact to permanent merger. The following taxonomy classifies field interactions by their structural characteristics:

| **Interaction Type** | **Definition** | **Structural Mechanism** | **Duration** |
|---|---|---|---|
| **Field Contact** | Two fields become aware of each other. Information crosses the boundary but neither field's internal structure is altered. | Cross-board Bridges with bridge_type: "reference". One field's artifacts are referenced by another field's participants, but no new artifacts are produced in either field as a result. | Transient. The bridge may persist as a reference but generates no ongoing interaction. |
| **Field Resonance** | Two fields discover structural alignment, such as shared dimensional positions, compatible pillar orientations, or complementary developmental phases, that produces mutual amplification. Each field's intelligence becomes more coherent through awareness of the other. | Cross-board Bridges with bridge_type: "resonance". Artifacts in each field gain operational significance (per Constraint 5, Resonant Activation) from awareness of structurally aligned artifacts in the other field. FieldState field_resonance in both fields increases. | Sustained as long as the alignment holds. May be disrupted by developmental divergence. |
| **Field Tension** | Two fields discover structural opposition, such as incompatible 5D identities, contradictory contextual frameworks, or competing gravitational centers, that creates charged interaction. Neither field can ignore the other without losing signal. | Cross-board Bridges with bridge_type: "tension". The tension model (Section 6, Field Tension) applies between fields as it does within them. Inter-field tension may be creative (producing synthesis artifacts in a third scope) or destructive (producing entrenchment in both fields). | Sustained until resolved, transcended, or the fields disengage. |
| **Field Merger** | Two fields combine into a single field. The artifacts, transitions, and bridges of both fields become part of a unified FieldState. This is not aggregation (placing artifacts side by side) but integration (the combined field exhibits emergent properties neither original field possessed). | Structural equivalent of a Board merge operation. The merger produces a new Snapshot capturing the combined state, and a Comparison analyzing how the merger transformed the intelligence landscape. *Facilitation guidance:* Merger requires explicit facilitation. Tension pairs between the formerly separate fields should be resolved, held, or explicitly acknowledged in the post-merger FieldState. | Permanent. The original fields cease to exist as independent entities, though they may be preserved as archived Branches for historical reference. |
| **Field Nesting** | One field operates within the context of a larger field. The inner field has its own FieldState but is influenced by (and influences) the outer field's conditions. Participants are inner fields operating within the board's field. Teams are inner fields operating within organizational fields. | The existing participant model (Section 1, Session) is already a field nesting implementation: each participant carries dimensional_affinity and dimensional_actual, which are properties of their individual field interacting with the board's field. Field nesting generalizes this pattern to any scale: boards nested within programs, programs nested within organizational fields, organizational fields nested within societal or ecological fields. | Ongoing. The nesting relationship persists as long as the inner field operates within the outer field's context. |

### 10.3 Inter-Field FieldState

When two fields interact, the interaction itself generates observable field health effects. These are not stored on either field independently. They are computed at the interaction boundary and are available when the two fields are evaluated together.

| **Inter-Field Metric** | **Description** |
|---|---|
| **boundary_permeability** | Float 0–1. How readily intelligence flows between the two fields. High permeability: bridges form easily, artifacts resonate across the boundary, participants move fluidly between fields. Low permeability: the fields operate in isolation despite proximity, bridges are sparse or reference-only, participants experience context-switching friction when moving between fields. Computed from cross-board bridge density, bridge types, and participant overlap. |
| **dimensional_alignment** | Object mapping each dimension (1D–9D) to an alignment score (float -1 to +1) between the two fields. +1 indicates both fields have strong, compatible activation at that dimension. -1 indicates both fields have strong, incompatible activation (tension). 0 indicates one or both fields have no activation at that dimension. The alignment profile reveals where the fields naturally resonate and where they naturally conflict. |
| **phase_compatibility** | Assessment of whether the two fields' evolution_phase values are compatible. Two fields in the same phase (both expanding, both consolidating) interact differently than fields in different phases (one expanding, one maturing). Phase compatibility influences whether Field Resonance or Field Tension is the more likely interaction outcome. |

### 10.4 Field Interaction Invariants

**INVARIANT:** Field interactions are governed by the same Pillar Metric that governs intra-field operations. A Bridge between fields must be justifiable through Heart (does this connection serve purpose?), Truth (is this connection structurally sound?), and Nuance (does this connection respect the complexity of both fields?). Field mergers must pass all three pillars or they produce Destructive Polarity at scale.

**INVARIANT:** Field nesting does not override inner-field autonomy. An organizational field may influence a board-level field through environmental signals (Section 1.2, Tier 3) and through facilitation intent, but it cannot directly re-tag, transition, or delete artifacts within the inner field. The inner field's structural integrity is governed by its own FieldState and its own facilitation contract. This mirrors the principle that participants (who are inner fields) contribute to the board's field but are not overwritten by it.

**INVARIANT:** Field interaction is recursive. Two fields interacting generate a third, emergent field at their boundary: the interaction field. This interaction field has its own FieldState (computed from inter-field metrics), its own dimensional characteristics, and its own evolution trajectory. The interaction field is not stored as a separate Board (unless the facilitator chooses to formalize it) but is recognized as a real structural phenomenon that produces intelligence neither contributing field could generate alone. This is Axiom 8 applied to Axiom 8: fields interacting generate fields.

**SCALE INVARIANT:** The field interaction types (Contact, Resonance, Tension, Merger, Nesting) apply at every scale the architecture operates. Two artifacts within a zone interact as micro-fields. Two zones within a section interact as meso-fields. Two boards within an organization interact as macro-fields. The structural mechanisms are identical; the complexity and facilitation requirements scale with the scope of the interaction. This invariant is the formal statement of the principle that the rules of field-to-field interaction are already defined in the dimensional structure. They are the same rules that operate within fields, applied recursively at increasing scale.

**WORKSPACE AS FIELD INTERACTION CONTAINER:** The Workspace (Section 1, Table 1) is the formal structural container for field-to-field dynamics at the multi-board scale. Where this section defines the theory of field interaction, the Workspace provides the object that implements it. Cross-board Bridges are scoped to a Workspace. Cross-board Comparisons draw Snapshots from Boards within the same Workspace. The Workspace's workspace_field_state is the inter-field FieldState described in Section 10.3, computed across all constituent Boards and their interactions. The Workspace does not govern the internal operations of its Boards (per the Field Nesting autonomy invariant above); it provides the scope within which their interactions are observable, measurable, and actionable. A Workspace with multiple Boards in Field Resonance is a portfolio aligned around a shared intelligence pattern. A Workspace with multiple Boards in Field Tension is a portfolio where competing strategies are being held and compared. Both are structurally healthy; the Workspace makes the pattern visible.

---

*DN Kernel v0.9.1 · © Travis Kahn · [DN Framework](https://dnframework.ai) · [GitHub](https://github.com/DeusNosMachina/DN_Framework) · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*
