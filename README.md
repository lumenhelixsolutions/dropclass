# dropclass

<p align="center">
  <a href="https://lumenhelix.com">
    <img src="docs/assets/lumenhelix-logo.svg" alt="LumenHelix Solutions" width="180">
  </a>
</p>

<h3 align="center">Agent formation engine that turns a MOOC syllabus into a verified talent</h3>

<p align="center">
  <a href="https://lumenhelixsolutions.github.io/dropclass/">
    <img src="https://img.shields.io/badge/Launch_Page-dropclass-00D4FF?style=flat-square&logo=githubpages&logoColor=white" alt="Launch Page">
  </a>
  <a href="https://lumenhelix.com">
    <img src="https://img.shields.io/badge/Built_by-LumenHelix-7C3AED?style=flat-square" alt="Built by LumenHelix">
  </a>
  <img src="https://img.shields.io/badge/license-MIT-8A95A8?style=flat-square" alt="License">
</p>

---

**dropclass** is part of the [LumenHelix Solutions](https://lumenhelix.com) portfolio — applied symbolic dynamics & reversible computation for deterministic, traceable AI systems.

DropClass is the LumenHelix agent formation engine. It discovers free online courses, enrolls an agent in a real curriculum, runs competency checks, and exports a persistent domain talent that generalizes beyond the source material. Designed to mount inside the Atelier portfolio shell.

## Why this exists

- **Learn from real syllabi.** Agents follow actual MOOC structures instead of invented curricula.
- **Measure what matters.** Competency and transfer tests prove the agent can solve unseen problems.
- **Own the loop.** Local-first Python package with reversible decisions and full traceability.

## Quick start

Install and run dropclass in under two minutes.

### macOS / Linux

```bash
# Clone
git clone https://github.com/lumenhelixsolutions/dropclass.git
cd dropclass

# Install & run
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
```

### Windows (PowerShell)

```powershell
# Clone
git clone https://github.com/lumenhelixsolutions/dropclass.git
Set-Location dropclass

# Install & run
python -m venv .venv
.venv\Scripts\activate
pip install -e '.[dev]'
pytest
```

### Windows (Git Bash / WSL)

```bash
git clone https://github.com/lumenhelixsolutions/dropclass.git
cd dropclass
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
```

> **Device note:** dropclass is tested on Windows 11, macOS Sonoma, Ubuntu 22.04/24.04, and modern mobile browsers.

## Full documentation

Visit the launch page for architecture, API reference, and deployment guides:  
**https://lumenhelixsolutions.github.io/dropclass/**

## Features

| Feature | What it gives you |
|---------|-------------------|
| MOOC discovery | Search Class Central for syllabi and free-audit paths across Coursera, edX, and YouTube. |
| Formation loop | Ingest materials, practice, get feedback, and consolidate memory into a transferable talent. |
| Competency + transfer tests | Verify domain ability with assessments and novel hold-out problems, not watch time. |
| Mounts in Atelier | FastAPI routes drop into the Atelier shell so the UI can supervise every enrollment. |

## Architecture at a glance

```
dropclass/
├── discovery/   Class Central search + catalog normalization
├── coursera/    Platform student loop (future)
├── formation/   Enrollment, memory, and talent store
└── api/         FastAPI routes mounted by Atelier
```

## Development

```bash
python -m venv .venv
.venv\Scripts\activate  # or source .venv/bin/activate
pip install -e '.[dev]'
pytest
```

## Roadmap

- [ ] Class Central HTML parser and real course metadata
- [ ] Coursera student loop with transcript + assignment ingestion
- [ ] Talent export format and Atelier supervisor dashboard

## Support & consulting

Need deterministic AI systems with full traceability? LumenHelix builds reversible computation kernels, governance layers, and end-to-end AI integrations.

- **Website:** https://lumenhelix.com
- **Services:** AI diagnostics, B.Y.O. support packages, governance audits
- **Research:** TEN² kernel, R.U.B.I.C. boundary discipline, C.O.R.E. constraint lens

## License

Released under the MIT License.

---

<p align="center">
  <sub>Engineered by <a href="https://lumenhelix.com">LumenHelix Solutions</a> — Applied Symbolic Dynamics & Reversible Computation.</sub>
</p>
