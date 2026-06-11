# Synthetic Image-Text Dataset Workflow with Codex

This repository is a practical reference for building a small, auditable
synthetic image-text dataset with Codex. It demonstrates how to move from a
written dataset contract to local placeholder generation, structured prompts,
reviewed synthetic images, matching observation text, and verified metadata.

The workflow is intentionally lightweight. It does not include a frontend,
database, VLM validation pipeline, or manual API integration.

All included images are synthetic and must not be presented as evidence from a
real inspection, institution, or location.

## Current Dataset Snapshot

| Artifact | Count |
| --- | ---: |
| JPEG images | 27 |
| Matching text comments | 27 |
| Metadata rows | 27 |
| Categories | 8 |

Current category distribution:

| Category | Records |
| --- | ---: |
| classroom | 3 |
| washroom | 7 |
| staircase | 3 |
| corridor | 3 |
| electrical_panel | 3 |
| ceiling | 3 |
| exterior_wall | 3 |
| fire_extinguisher | 2 |

## Repository Structure

```text
AGENTS.md
PLAN.md
README.md
image-gen-prompts.md
image-gen-prompts-indian-ngo-school.md

scripts/
  generate_sample_dataset.py

data/
  metadata.csv
  sample_images/
  sample_comments/
  placeholder_image_backup/
```

- `AGENTS.md` defines repository rules, safety constraints, and dataset
  invariants.
- `PLAN.md` defines the repeatable process for future additions or image
  replacements.
- `scripts/generate_sample_dataset.py` creates the deterministic local
  placeholder baseline.
- `image-gen-prompts.md` is a generic prompt inventory.
- `image-gen-prompts-indian-ngo-school.md` is a preserved domain-specific
  prompt-inventory example.
- `data/metadata.csv` connects every image to its category, scenario, labels,
  summary, and comment.

## Dataset Contract

Every record consists of:

```text
data/sample_images/<stem>.jpg
data/sample_comments/<stem>.txt
one matching row in data/metadata.csv
```

For example:

```text
data/sample_images/washroom_001.jpg
data/sample_comments/washroom_001.txt
```

The filename stem is the stable identity that joins all artifacts.

`data/metadata.csv` uses this exact column order:

```text
filename,category,scenario_type,issue_present,issue_type,issue_summary,comment_file
```

Comments are short plain-text observations. They describe visible details only,
avoid confidence scores and model-like language, and do not claim hidden
causes.

## How the Dataset Was Built

### 1. Define Rules Before Implementation

The project began by creating `AGENTS.md` before writing the generator. This
established:

- Exact folders and metadata columns.
- Stable image/comment filename stems.
- Scenario and issue-label conventions.
- Short visible-observation comments.
- Local-only placeholder generation.
- Safety and scope boundaries.

Separating the contract from implementation made later verification much
simpler.

### 2. Write an Explicit Execution Plan

`PLAN.md` was introduced before generating or replacing images. The plan made
the process incremental:

1. Define records.
2. Validate metadata and comments.
3. Prepare one prompt per image.
4. Back up existing images.
5. Generate and visually review candidates.
6. Replace files without changing their identities.
7. Verify the complete dataset.

This approval-first pattern is useful whenever generation may overwrite or
reinterpret existing data.

### 3. Create a Local Placeholder Baseline

`scripts/generate_sample_dataset.py` uses local Python and Pillow to create
simple non-photorealistic placeholder images, matching comments, and metadata.
Pillow is imported lazily so dry runs work even when it is not installed.

The generator supports:

```bash
uv run python scripts/generate_sample_dataset.py --count-per-category 1
uv run python scripts/generate_sample_dataset.py --count-per-category 3
uv run python scripts/generate_sample_dataset.py --count-per-category 3 --dry-run
uv run python scripts/generate_sample_dataset.py --count-per-category 3 --force
```

The base generator intentionally rejects values above three per generated
category. Its dry run prints planned images, comments, and metadata without
creating them.

Use `--force` carefully: it can overwrite curated dataset files with local
placeholders.

### 4. Build and Refine Prompt Inventories

The first prompt inventory, `image-gen-prompts.md`, translated each metadata row
and matching comment into a generic scene prompt. Each prompt section recorded:

- Target filename.
- Category and scenario.
- Issue presence, type, and summary.
- Matching comment.
- Image-generation prompt.
- Negative instructions.
- Replacement status.

Prompts were then refined for a specific domain in
`image-gen-prompts-indian-ngo-school.md`. Keeping generic and domain-specific
inventories separate demonstrates how the same dataset contract can support
different visual contexts without changing filenames or labels.

For a public or reusable prompt inventory, describe observable conditions and
avoid implying blame, ownership, funding, neglect, or socioeconomic status.

### 5. Pilot Before Scaling

A small category-level pilot was generated first. Each existing placeholder was
backed up, generated candidates were visually inspected, and only accepted
images replaced their exact original paths.

One candidate was rejected because it contained potentially readable text.
This reinforced an important lesson: prompts reduce risk, but human review is
still required.

### 6. Complete the Dataset Incrementally

After the pilot passed, the remaining planned images were processed category by
category. Later, a small number of explicitly requested washroom and
fire-extinguisher records were added with matching comments and metadata.

The current dataset therefore contains the original generated baseline plus
curated extensions. The generator's three-per-category cap remains unchanged;
the extensions were added through a separate, reviewed workflow.

### 7. Verify After Every Change

The final checks included:

- Equal image, comment, and metadata-row counts.
- Matching image/comment stems in both directions.
- Existing files for every metadata reference.
- No duplicate filenames.
- Readable JPEG files.
- Accurate visible-condition labels and comments.
- Preserved placeholder backups.
- No secrets, `.env`, environment-variable access, or manual API integration.

## Reusing This Workflow

1. Define a small dataset contract in `AGENTS.md`.
2. Write a step-specific plan and review it before execution.
3. Choose stable filename stems and a simple metadata schema.
4. Generate a deterministic local placeholder baseline.
5. Dry-run and verify before writing files.
6. Create exactly one prompt per intended image.
7. Keep prompts, comments, and metadata aligned.
8. Pilot a small batch before scaling.
9. Back up existing assets before replacement.
10. Visually inspect every generated candidate.
11. Add records incrementally and verify after every batch.
12. Document the final counts, limitations, and intended use.

## Responsible Dataset Practices

- Clearly label synthetic content as synthetic.
- Do not use generated images as evidence about real people or places.
- Avoid identifiable people, private information, logos, or readable sensitive
  text unless the project explicitly requires and permits them.
- Describe visible facts rather than inferring hidden causes or intent.
- Avoid stereotypes and sensationalized conditions.
- Preserve provenance through prompts, metadata, comments, backups, and review
  notes.
- Treat generated labels as hypotheses until they are reviewed.

## Requirements

- Python 3.10 or newer.
- `uv` for project-local Python dependency management.
- Pillow for real placeholder generation.

Install Pillow locally with:

```bash
uv add pillow
```

Then begin with a dry run:

```bash
uv run python scripts/generate_sample_dataset.py --count-per-category 1 --dry-run
```

## Intended Use

This repository is suitable for learning and prototyping:

- Synthetic image-text dataset construction.
- Image/comment/metadata joins.
- Prompt refinement and controlled generation.
- Human-in-the-loop visual quality review.
- Dataset integrity checks before VLM experiments.

It is a workflow example, not a benchmark, production validation system, or
source of real-world inspection evidence.
