# DropClass — Agent Learning Formation

**Path:** `D:/projects/dropclass/`

DropClass explores whether autonomous agents can acquire **talents** (domain judgment and transferable capability) by following free online courses discovered via [Class Central](https://www.classcentral.com/).

## Core thesis

- **Skills** are narrow tools. **Talents** are how an agent *thinks* in a field after structured study.
- Class Central is the **catalog**; actual learning happens on provider sites (Coursera, edX, YouTube, university pages).
- Success is measured by **competency** and **transfer tests**, not certificates alone.

## Key docs

| Doc | Path |
|-----|------|
| Vocabulary | `CONCEPTS.md` |
| Requirements brainstorm | `notes/brainstorms/2026-06-22-dropclass-requirements.md` |
| MVP plan | `notes/plans/2026-06-22-dropclass-mvp-plan.md` |

## Product shape

**Not a standalone product.** DropClass is a **Python service + React module** inside a **new shared portfolio shell** (greenfield host — name TBD):

| Layer | Role |
|-------|------|
| **Shell** | [Atelier](../atelier/) — React + Python host; DropClass is first feature route |
| **dropclass/** | Python formation engine + React feature module (enroll, progress, competency, approvals) |
| **Agent** | Coursera student loop, ingest, assessments; UI supervises, agent executes |

No `dropclass.app` — shell is the product surface; DropClass is a module.

## Status

Exploration / feasibility — no implementation yet.