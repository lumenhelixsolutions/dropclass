# DropClass — Requirements Brainstorm

**Date:** 2026-06-22  
**Status:** Draft — exploration  
**Vocabulary:** `CONCEPTS.md`

---

## Problem

People and teams want agents that don't just *use* tools — they want agents that have **studied** something: epidemiology, cartography, negotiation, accounting. Today we give agents skills (narrow functions). We want something closer to hiring a junior specialist who took the course.

**DropClass** asks: can we send an agent through a free MOOC (discovered on Class Central) and emerge with a durable **talent** it can apply later?

---

## What Class Central actually is

Class Central is a **search engine and catalog** for online courses. It links out to providers:

- Coursera, edX, Udacity, university sites, YouTube playlists, etc.
- Free, audit-only, and certificate tracks vary per provider
- Class Central does **not** host videos, quizzes, or grades

**Implication:** DropClass must solve *provider integration*, not "scrape Class Central and learn." Class Central is the **discovery layer**.

---

## Skill vs talent (working definition)

| | Skill | Talent |
|---|--------|--------|
| Scope | One task | A domain |
| Durability | Swappable | Persistent persona/module |
| Proof | Runs without error | Transfer test on novel problems |
| Example | "Summarize this PDF" | "Reason about outbreak data like an epi student" |

**Formation** is the pipeline: catalog → curriculum → practice → assessment → talent module.

---

## Feasibility — what breaks

### Easy-ish
- Discover free courses by subject on Class Central
- Parse public syllabi and learning outcomes
- Ingest open materials (YouTube CC, MIT OCW, edX audit transcripts where available)
- Build RAG / memory over lecture content
- Generate practice questions and rubric-based grading locally

### Hard
- Unified login across Coursera/edX/etc.
- Browser automation through dynamic UIs, CAPTCHAs, paywalls
- Timed/proctored exams
- Peer-graded assignments requiring human classmates
- Terms of service on automated enrollment

### Wrong metric
- "Agent earned a certificate" — gameable, brittle, provider-specific
- Better: **competency rubric + transfer test** on held-out problems

---

## Approaches

### A. Curriculum Compiler (recommended MVP)

**Shape:** Class Central finds candidates → human or agent picks one → DropClass **replicates the syllabus locally** using openly accessible materials (transcripts, readings, labs) → agent completes formation loop offline from platform accounts.

| Pros | Cons |
|------|------|
| Legal/ToS safer | Not every course has open transcripts |
| Provider-agnostic core | No official certificate |
| Measurable via transfer tests | Syllabus mapping is manual at first |
| Fits agent-native loops (ingest → practice → assess) | |

**Best for:** Proving the talent model before touching platform automation.

### B. Synthetic Classroom

**Shape:** Same as A, plus simulated cohort: discussion prompts, Socratic tutor, project critiques, spaced repetition schedule. Talent export = prompt module + memory graph + competency scores.

| Pros | Cons |
|------|------|
| Closer to "took the class" psychologically | More product surface area |
| Can exceed MOOC quality with good tutoring | Harder to validate against real course |

**Best for:** Product differentiation if A shows competency gains.

### C. Full Autonomous Student (defer)

**Shape:** Browser agent enrolls on provider, watches videos, submits quizzes, earns certs.

| Pros | Cons |
|------|------|
| Impressive demo | Fragile, high maintenance |
| Real certificate | ToS / ethics risk |
| | Proctoring, peer review blockers |

**Best for:** Later, scoped to one provider with official API — not Class Central-wide.

---

## User direction (2026-06-22)

Primary goal is **Coursera certificate completion**, not synthetic assessment alone. That pushes toward **Approach C**, but Coursera-specific constraints apply (see below).

## Recommended direction (phased — cert goal)

Even with certs as the north star, ship in phases:

**Phase 0 — Discovery:** Class Central → Coursera course shortlist (free audit + cert-eligible).

**Phase 1 — Coursera student loop (MVP):** Browser agent on *one* Coursera specialization week: watch (or transcript), attempt quizzes, track gradebook locally. Measure quiz pass rate.

**Phase 2 — Full cert:** Payment flow (human-in-loop), honorlock/proctoring gaps documented, peer assignments where required.

**Parallel track (de-risk):** Approach A on same syllabus so formation continues when UI automation breaks.

Original **Approach A** vertical slice still applies as fallback:

1. Pick a free course with rich open content (e.g. YouTube + readings)
2. Build: catalog pick → syllabus → ingest → daily formation sessions → transfer test
3. Export a **talent profile** (vocabulary, heuristics, exemplar reasoning chains)
4. Measure: does a downstream task (novel problem in domain) improve vs base model?

If transfer tests pass, Approach B adds polish. Approach C stays out of scope until a single provider justifies it.

---

## MVP scope (proposed)

### In scope
- Class Central discovery helper (subject → ranked free candidates)
- Manual confirm of one course
- Syllabus + unit tracker
- Material ingest (transcript/text)
- Formation loop: read → summarize → practice → assess
- Competency score + transfer test bank
- Talent profile artifact on disk

### Out of scope (v1)
- Multi-provider browser automation
- Certificate farming
- Peer-graded assignment submission
- Fine-tuning / weight updates (memory + prompts first)

### Resolved (dialogue)
- **Primary success metric:** Platform completion — agent passes quizzes and earns certificate on the original provider
- **First provider:** Coursera
- **Product shape:** Not a standalone DropClass product — **Python backend + React UI module** in a **new shared portfolio shell** (greenfield host app)
- **Interaction:** React/Python web UI for enrollment, progress, competency — agent does the work; human supervises
- **Host:** **Atelier** (`../atelier/`) — greenfield React + Python shell
- **Shell v1 scope:** DropClass-first — shell exists mainly to run agent formation; other portfolio modules deferred

### Open questions
- Who is the user — solo dev, team lead, product builder?
- Integrate with HOOT as agent profile, or standalone app?
- Accept "audit-only" courses with no quizzes as formation with synthetic assessment?

---

## Success criteria (draft)

1. Agent completes one real MOOC syllabus (≥80% units) using open materials
2. Transfer test score ≥ human "week-1 student" baseline on 10 held-out problems
3. Talent profile measurably improves downstream task quality vs no formation
4. Documented feasibility matrix for top 5 Class Central provider types

---

## Dependencies / assumptions

- Most value is in **open** or **transcript-available** courses
- Formation quality depends more on practice + feedback than passive watching
- "Talent" is initially a **portable prompt + memory package**, not weight training
- Class Central HTML/API may change; discovery layer should be replaceable

---

## Next step

- Plan: `docs/plans/2026-06-22-dropclass-mvp-plan.md`
- Shell scaffold: `../atelier/`
- Execute: `/ce-work` from IU-2