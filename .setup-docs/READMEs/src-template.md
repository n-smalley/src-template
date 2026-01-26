# Project Template Structure Overview

This repository is a **Python project template** designed to support:
- repeatable project setup
- consistent source code organization
- separation of data, scripts, and outputs
- easy onboarding for new projects and teammates

Below is an explanation of each top-level directory and the intended usage patterns.

---

## Root Level
```text
C:.
├── .gitignore
├── tree.txt
├── .setup-docs/
├── archive/
├── batch/
├── data/
├── scripts/
├── src/
└── work/
```

### `.gitignore`
Standard Git ignore file.  
Used to prevent committing:
- virtual environments
- temporary files
- secrets
- generated outputs

---

## `.setup-docs/` — Project Bootstrapping & Documentation

This folder contains **project setup tooling and reference documentation**.  
It is not meant to be modified per-project once established.
```text
.setup-docs/
├── .venv_setup.bat
├── create_project.py
├── LICENSE
├── requirements.txt
├── READMEs/
└── src-template/
```
### `.venv_setup.bat`
Windows batch script for:
- creating a virtual environment
- installing dependencies
- standardizing environment setup

### `create_project.py`
Script that:
- run `python .setup-docs\create_project.py project-name` in terminal
- scaffolds a new project
- copies the `src-template`
- replaces `{{PROJECT_NAME}}` placeholders
- sets up consistent naming and paths
- creates basic script at `scripts\run_project-name.py`
    - converts '-' to '_' within file for syntax

### `requirements.txt`
Dependencies required for:
- running setup scripts
- generating projects


### `READMEs/`
Centralized documentation for contributors and new users.
```text
READMEs/
├── git_workflow.md
├── src-template.md
└── venv_setup.md
```
- **git_workflow.md** — collaboration and branching strategy
- **src-template.md** — explanation of the Python source layout
- **venv_setup.md** — instructions for environment setup

### `src-template/`
This is the **blueprint** for new projects.
```text
src-template/
└── {{PROJECT_NAME}}/
```
`{{PROJECT_NAME}}` is replaced during project creation.

The structure inside mirrors the real project under `src/`.

---

## `archive/` — Long-term Storage

Intended for:
- deprecated outputs
- frozen datasets
- old results kept for reference

**Not actively modified**

---

## `batch/` — Batch / Automation Assets

Used for:
- batch files
- scheduled jobs
- automation helpers
- system-level scripts

Kept separate from Python runtime code.

---

## `data/` — Raw & Input Data
```text
data/
├── csv/
├── json/
└── xlsx/
```
This directory stores **source data only**.

Best practices:
- treat as read-only
- no business logic here
- no derived outputs
- i/o should deposit here

Additional folders can be added as needed.

---

## `scripts/` — Entry-Point Scripts
```text
scripts/
└── run_example_project.py
```

Scripts here:
- orchestrate workflows
- call into `src/`
- act as command-line or execution entry points

They should **not contain core logic**, only coordination.

---

## `src/` — Application / Library Code

This is the **main Python codebase**.
```text
src/
└── example_project/
```
Each project lives in its own top-level package.

### Core Files
```text
example_project/
├── config.py
├── paths.py
├── utils.py
```
- **config.py**  
  - Central configuration values (constants, settings, toggles)

- **paths.py**  
  - Canonical filesystem paths (data dirs, output dirs, etc.)  
  - Helps avoid hardcoded paths across the codebase.

- **utils.py**  
  - Shared helper functions used across modules

### Subpackages (Layered Architecture)
These should serve as examples or a baseline. Add new Subpackages as needed or deletee those that are not needed.
```text
├── analysis/
├── cli/
├── io/
├── processing/
└── reporting/
```
#### `analysis/`
- exploratory or analytical logic
- metrics, modeling, investigation
- domain-level reasoning

#### `cli/`
- command-line interface
- organizes all the other packages into the actual logical structure and is called by `scripts\run_project-name.py`

Example: `cli\main.py`

#### `io/`
- input / output
- reading and writing data
- serialization / deserialization
- file and format handling

Keeps I/O concerns isolated.

#### `processing/`
- transformation pipelines
- data cleaning
- core business logic

This is often the “engine” of the project.

#### `reporting/`
- report generation
- summaries
- plots or formatted outputs

Separates results from computation.

---

## `work/` — Scratch Space
```text
work/
└── temporary/
```
Used for:
- experiments
- local testing
- intermediate outputs
- throwaway files

Typically **gitignored** or partially ignored.

---

## About `__init__.py` (General Explanation)

Although omitted above for brevity:

- `__init__.py` marks a directory as a Python package
- enables imports across modules
- allows controlled exposure of package APIs
- supports relative imports

They are intentionally minimal to keep package boundaries clean.

---

## Design Principles Behind This Template

### **Separation of concerns**
Each part of the repository has a single, well-defined responsibility.  
Source code, data, setup tooling, scripts, and outputs are intentionally separated so that:
- changes in one area do not unintentionally affect others
- code remains easier to understand, test, and refactor
- responsibilities are clear to both humans and tooling

This reduces cognitive load and helps prevent tightly coupled, fragile project structures.

### **Repeatable project creation**
The template is designed to make new projects predictable and fast to spin up.  
By using a standardized layout and automated scaffolding:
- every project starts from the same baseline
- setup steps are minimized and documented
- structure and conventions are consistent across projects

This repeatability improves onboarding, reduces setup errors, and allows teams to focus on solving problems instead of configuring projects.

### **Clear boundaries between data, code, and outputs**
The repository enforces explicit boundaries:
- **data** is treated as input and reference material
- **code** is versioned, importable, and testable
- **outputs and temporary artifacts** are kept out of the core source tree

These boundaries make it easier to reason about project state, avoid accidental data loss or corruption, and ensure that version control remains clean and meaningful.

### **Scales from single-user to team collaboration**
The structure works equally well for solo experimentation and multi-person collaboration.  
Clear conventions around where things live:
- reduce merge conflicts
- make pull requests easier to review
- eliminate reliance on undocumented tribal knowledge

As the team grows, the structure remains stable instead of needing repeated reorganization.

### **Supports scripting, CLI usage, and library-style imports**
The template supports multiple interaction patterns without code duplication:
- **scripts** for quick execution and automation
- **CLI entry points** for structured command-line workflows
- **library-style imports** for reuse, testing, and composition

This allows the same core logic to be reused across different contexts, making the project more flexible, maintainable, and extensible over time.