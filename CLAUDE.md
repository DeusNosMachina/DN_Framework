# DN Framework: instructions for AI agents

This repository is the canon of the DN Framework. Everything else that speaks DN is downstream of it. `README.md` maps the folders, and each folder has its own README.

## Rules

- **The Kernel governs.** `kernel/DN_Kernel.md` is the structural constitution and `kernel/DN_Glossary_of_Terms.md` standardizes every term. When anything in this repo disagrees with the Kernel, the Kernel is right and the other thing gets fixed.
- **Never redefine a term or reduce the model.** Use Glossary definitions as written. Do not paraphrase an invariant into something softer.
- **A Kernel or Glossary change is the author's decision.** Propose it with its reasoning. Do not make it in passing while working on something else. A change is versioned and recorded in the changelog, and it has consequences for every product and site built on the framework.
- **Skills are read directly by live agent sessions.** The files in `skills/` are linked into agent tooling, not copied, so an edit takes effect wherever the skill is installed. Keep each skill self-contained and grounded in the Kernel and Glossary.
- **Human-exclusive functions stay human.** Signal Lock attestation, Shadow confrontation, holding space under collapse and ethical override are never delegated to an AI. An agent may flag a candidate. It never applies the lock.
- **Shadow is orientation, not failure.** No pejorative treatment.
- **Honest assessment beats validation.** When reviewing or extending the framework, name the weak spots plainly. The framework is not a proving ground for itself.
- **This repository is public.** Nothing private belongs in it: no client names, no engagement material, no internal strategy.
- Don't put status in this file. Each folder's README and the changelogs carry it.
