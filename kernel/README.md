# Kernel

**Governing documents of the DN Framework.**

The kernel contains the canonical, authoritative documents that define what the DN Framework *is* — its invariants, constraints, terminology, and structural requirements. All other documents, applications, and products built on the DN Framework reference the kernel by section number and use its glossary terms as defined here.

---

## Contents

### DN Kernel (`DN_Kernel.md`)

The machine-readable specification of the DN Framework. Defines:

- The nine dimensions of intelligence and their properties
- The three foundational pillars (Heart, Truth, Nuance)
- Structural invariants and constraints that must hold in any DN implementation
- Signal architecture and source type classification
- Transition mechanics and evidence requirements
- Simulation command contracts
- Commit gate definitions
- Human-exclusive function boundaries

The `.md` format is the **canonical version** — it renders directly on GitHub and is optimized for machine consumption by AI systems.

### DN Glossary of Terms (`DN_Glossary_of_Terms.md` / `.docx`)

The standardized lexicon of the DN Framework. Every term used across the corpus, Growth Blueprint, and any DN-derived product is defined here with:

- Practical and conceptual definitions
- Pillar affiliations (Heart / Truth / Nuance)
- Dimensional color codes
- Symbolic tags (e.g., 🔒 Signal Lock)

The `.md` is the canonical version for GitHub and AI consumption. The `.docx` is provided for offline reading and download.

### CHANGELOG (`CHANGELOG.md`)

Version history of the DN Kernel, tracking revisions, additions, and structural changes to the governing specification.

---

## Usage

When referencing kernel content from other documents or implementations, use the convention:

> per Kernel §X.Y

Never embed kernel content directly — always reference by section number. This ensures that as the kernel evolves, all references remain traceable to a specific version and section.
