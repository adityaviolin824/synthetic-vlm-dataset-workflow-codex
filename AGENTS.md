# Repository Working Rules

## Purpose

This repository demonstrates a small, auditable workflow for creating paired
synthetic images, plain-text observations, and structured metadata. It is
intended as a reusable reference for dataset prototyping, VLM experiments, and
other multimodal projects.

All images in this repository are synthetic. Do not present them as evidence
from a real inspection, institution, or location.

## Safety and Scope

- Never expose or use secrets.
- Do not access `.env` files or read environment variables.
- Do not make manual API calls or add API integrations unless the user
  explicitly changes the project scope.
- Do not add frontend, VLM validation, database, or unrelated architecture
  unless explicitly requested.
- Keep changes incremental, simple, and easy to verify.
- Do not modify a domain-specific prompt inventory unless the user explicitly
  asks for that file to be changed.

## Python Workflow

- Use `uv` for Python environment and dependency management.
- Use `uv run` instead of invoking project Python directly.
- Use `uv add` instead of `pip install`.
- Prefer project-local dependencies and a project-local `.venv`.

## Dataset Structure

```text
data/
  sample_images/
  sample_comments/
  metadata.csv

scripts/
  generate_sample_dataset.py
```

Local replacement work may use the ignored
`data/placeholder_image_backup/` directory. It is not part of the published
repository structure.

Every image must have a matching comment file with the exact same filename
stem.

Example:

```text
data/sample_images/washroom_001.jpg
data/sample_comments/washroom_001.txt
```

## Dataset Contract

`data/metadata.csv` uses this exact column order:

```text
filename,category,scenario_type,issue_present,issue_type,issue_summary,comment_file
```

Required invariants:

- `filename` identifies an existing image in `data/sample_images/`.
- `comment_file` identifies an existing comment in `data/sample_comments/`.
- Image and comment filename stems match.
- `issue_present` is `true` or `false`.
- Normal records use `scenario_type = normal_no_issue`,
  `issue_present = false`, and `issue_type = none`.
- Comments describe visible observations only and do not claim hidden causes.
- Comments are plain text, one to three sentences, without confidence scores or
  model-like language.

## Current Dataset

The current curated dataset contains 27 image-comment-metadata records across:

```text
classroom
washroom
staircase
corridor
electrical_panel
ceiling
exterior_wall
fire_extinguisher
```

The base local generator creates up to three records for each of its seven
original categories. Its `--count-per-category` argument must continue to reject
values above three. Curated records added after base generation may extend a
category or introduce a new category only when explicitly requested and after
all dataset invariants are verified.

## Local Placeholder Generator

`scripts/generate_sample_dataset.py`:

- Uses only local Python and Pillow/PIL.
- Lazily imports Pillow so dry runs work without Pillow installed.
- Generates simple placeholder images, not photorealistic scenes.
- Creates matching comments and metadata rows.
- Does not overwrite existing generated files unless `--force` is passed.
- Must not use APIs, `.env`, environment variables, or secrets.

Supported commands:

```bash
uv run python scripts/generate_sample_dataset.py --count-per-category 1
uv run python scripts/generate_sample_dataset.py --count-per-category 3
uv run python scripts/generate_sample_dataset.py --count-per-category 3 --dry-run
uv run python scripts/generate_sample_dataset.py --count-per-category 3 --force
```

Use `--force` only when intentionally replacing existing generated files. It
can overwrite curated dataset content.

## Prompt Inventories and Image Replacement

- Treat metadata and comments as the authoritative label contract.
- Keep exactly one prompt section per intended image replacement.
- Ensure each prompt matches its metadata row and comment before generation.
- Describe observable visual conditions without inferring ownership, funding,
  blame, neglect, or hidden causes.
- Avoid stereotypes, sensational damage, and identifiable people or private
  information.
- Back up an existing image before replacing it.
- Preserve exact filenames and `.jpg` extensions.
- Visually inspect generated candidates before accepting them.
- Update replacement status only after a replacement passes inspection.

## Verification

After any dataset change, verify:

1. Every metadata image and comment file exists.
2. Every image has a matching comment stem.
3. Every comment has a matching image stem.
4. Metadata row count matches image and comment counts.
5. There are no duplicate filenames or comment filenames.
6. Every image opens successfully as JPEG.
7. Metadata and comments accurately describe visible image content.
8. No secrets, `.env`, environment-variable access, API integration, or
   unrelated architecture was added.

## Codex Behavior

1. Read this file before changing the repository.
2. Read `PLAN.md` before expanding or replacing dataset content.
3. Work incrementally and validate each step.
4. Do not overwrite backups or authoritative labels without explicit approval.
5. Do not modify ignored local prompt inventories unless explicitly requested.
6. Stop and ask when a requested image conflicts with its metadata or comment.
