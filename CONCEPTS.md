# DropClass — Domain Vocabulary

Authoritative terms for this project. Use these names in docs, prompts, and code.

## Skill

An atomic, callable capability an agent can invoke for a narrow task.
Examples: summarize a transcript, extract dates from text, run a unit test.

Skills are **procedural** and **replaceable** — swapping one summarizer for another barely changes agent behavior.

## Talent

A persistent, transferable way of thinking and working in a domain, acquired through structured study and practice.
A talent bundles vocabulary, mental models, heuristics, worked examples, and judgment — not just facts.

Examples: "thinks like an epidemiologist," "reads a balance sheet like an analyst," "designs maps like a cartographer."

Talents are **identity-level** for the agent: they change how it approaches *unseen* problems in that domain.

## Formation

The process of acquiring a talent by following a curriculum: ingest materials, practice, get feedback, consolidate memory.

DropClass **drops** an agent into formation for a chosen course or learning path.

## Curriculum

A structured sequence of learning units (lectures, readings, labs, assessments) with stated learning outcomes.
Usually sourced from a MOOC syllabus, not invented by the agent.

## Competency

Demonstrated ability in a domain, verified by assessment — not by hours watched or pages read.

Competency is how we **measure** whether formation produced a talent.

## Catalog

An index of discoverable learning opportunities. [Class Central](https://www.classcentral.com/) is a catalog aggregator; it does not host course content.

## Enrollment

Committing an agent to a specific curriculum with goals, schedule, and success criteria.
Enrollment may be **synthetic** (we replicate the syllabus locally) or **platform** (agent acts on Coursera/edX/etc.).

## Transfer test

Novel problems in the target domain, held out from course materials, used to verify the talent generalizes beyond memorization.

## Shell (Atelier)

The **Atelier** app (`../atelier/`) — greenfield React + Python host. DropClass mounts as the `/formation` feature. Other portfolio modules may plug in later.