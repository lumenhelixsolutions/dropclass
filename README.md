# dropclass

<p align="center">
  <img src="docs/assets/logo.svg" alt="dropclass logo" width="160">
</p>

<h3 align="center">Syllabus to talent.</h3>

<p align="center">Agent formation engine that turns a MOOC syllabus into a verified, transferable domain skill.</p>

<p align="center">
  <a href="https://lumenhelixsolutions.github.io/dropclass/">Launch Page</a>
  <span> · </span>
  <a href="https://github.com/lumenhelixsolutions/dropclass">GitHub</a>
  <span> · </span>
  <a href="https://lumenhelix.com">LumenHelix</a>
</p>

---

DropClass is the LumenHelix agent formation engine. It discovers free online courses, enrolls an agent in a real curriculum, runs competency checks, and exports a persistent domain talent that generalizes beyond the source material. Designed to mount inside the Atelier portfolio shell.

## Why dropclass

- **Learn from real syllabi.** Agents follow actual MOOC structures instead of invented curricula.
- **Measure what matters.** Competency and transfer tests prove the agent can solve unseen problems.
- **Own the loop.** Local-first Python package with reversible decisions and full traceability.

## Quick start

### macOS / Linux

```bash
git clone https://github.com/lumenhelixsolutions/dropclass.git
cd dropclass
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
```

### Windows (PowerShell)

```powershell
git clone https://github.com/lumenhelixsolutions/dropclass.git
Set-Location dropclass
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

> Tested on Windows 11, macOS Sonoma, Ubuntu 22.04/24.04, and modern mobile browsers.

## Features

| Feature | What it gives you |
|---------|-------------------|
| MOOC discovery | Search Class Central for syllabi and free-audit paths across Coursera, edX, and YouTube. |
| Formation loop | Ingest materials, practice, get feedback, and consolidate memory into a transferable talent. |
| Competency + transfer tests | Verify domain ability with assessments and novel hold-out problems, not watch time. |
| Mounts in Atelier | FastAPI routes drop into the Atelier shell so the UI can supervise every enrollment. |

## Architecture

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

## License

Released under the MIT License.

---

<p align="center">
  <sub>dropclass is a <a href="https://lumenhelix.com">LumenHelix</a> project — Applied Symbolic Dynamics & Reversible Computation.</sub>
</p>
