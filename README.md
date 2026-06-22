# DropClass

Send an AI agent through a free online course — and measure whether it gained a **talent**, not just a skill.

**Catalog:** [Class Central](https://www.classcentral.com/) (discovery only — courses live on Coursera, edX, YouTube, etc.)

## Idea in one sentence

DropClass drops an agent into **formation** for a real MOOC syllabus, then exports a persistent domain **talent** verified by competency and transfer tests.

## Docs

- [`CONCEPTS.md`](CONCEPTS.md) — skill vs talent vocabulary
- [`docs/brainstorms/2026-06-22-dropclass-requirements.md`](docs/brainstorms/2026-06-22-dropclass-requirements.md) — feasibility brainstorm

## Architecture (decided)

- **Shell:** [Atelier](../atelier/) — React + Python host (DropClass-first v1)
- **DropClass:** formation engine package in this repo
- **Agent:** Coursera student loop; UI supervises

## Plan

[`docs/plans/2026-06-22-dropclass-mvp-plan.md`](docs/plans/2026-06-22-dropclass-mvp-plan.md)

## Status

Exploration — June 2026