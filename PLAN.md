# Reusable Synthetic Image-Text Dataset Plan

## Status

The baseline dataset and its approved curated extensions are complete. This
plan defines the repeatable process for future additions or replacements.

Current verified snapshot:

```text
27 JPEG images
27 text comments
27 metadata rows
8 categories
```

## Goal

Create or extend a small synthetic image-text dataset while preserving a clear
contract between each image, its observation text, and its metadata row.

The process should remain auditable, incremental, and suitable for later VLM or
multimodal experiments without adding application architecture.

## Authoritative Contract

For every record:

- `data/metadata.csv` defines the filename, category, scenario, issue label,
  issue summary, and comment filename.
- `data/sample_comments/` contains the matching visible-observation text.
- `data/sample_images/` contains the matching JPEG image.
- Image and comment filename stems must match exactly.
- Metadata and comments must accurately describe the visible image.

## Hard Constraints

- Do not use secrets, `.env`, or environment variables.
- Do not make manual API calls or add API integrations.
- Do not rename existing dataset files.
- Do not overwrite placeholder backups.
- Do not modify authoritative metadata or comments merely to excuse a poor
  image match.
- Do not add frontend, VLM validation, database, or unrelated architecture.
- Do not modify a domain-specific prompt inventory unless explicitly asked.

## Workflow

### 1. Define the Record

Before generating an image:

1. Choose a stable filename stem.
2. Define category, scenario type, issue presence, issue type, and concise
   issue summary.
3. Write a one-to-three-sentence observation describing only visible details.
4. Add or approve the metadata row and matching comment filename.

### 2. Prepare the Prompt

1. Write one prompt section for the intended image.
2. Include the exact filename and matching dataset labels.
3. Describe scene context, visible condition, severity, and composition.
4. Add negative instructions that prevent text overlays, identifiable people,
   private information, logos, sensational damage, and unrelated details.
5. Avoid claims about hidden causes, ownership, funding, neglect, or social
   conditions.

### 3. Validate Before Generation

1. Confirm the target metadata row and comment agree.
2. Confirm no image, comment, or metadata filename is duplicated.
3. Confirm the prompt describes the same visible condition.
4. If replacing an image, record its hash and copy it to
   the ignored local `data/placeholder_image_backup/` directory without
   overwriting an existing backup.

### 4. Generate and Review

1. Generate one candidate at a time.
2. Visually inspect the candidate against the prompt, metadata, and comment.
3. Reject candidates with invented defects, identifiable people, readable
   private text, overlays, logos, stereotypes, or mismatched severity.
4. Save an accepted image as JPEG at the exact approved dataset path.
5. Update prompt replacement status only after the image passes review.

### 5. Verify the Dataset

After each batch:

1. Count images, comments, and metadata rows.
2. Verify matching stems in both directions.
3. Verify every metadata reference exists.
4. Verify uniqueness of image and comment filenames.
5. Open every new JPEG to confirm it is readable.
6. Confirm labels and comments match visible content.
7. Confirm protected files and backups were not unintentionally changed.

## Base Placeholder Generator

The local Pillow generator creates the original seven-category baseline and
allows at most three records per generated category:

```bash
uv run python scripts/generate_sample_dataset.py --count-per-category 3 --dry-run
uv run python scripts/generate_sample_dataset.py --count-per-category 3
```

Do not run it with `--force` unless intentionally rebuilding placeholders,
because that option can overwrite curated images, comments, and metadata.

## Completion Report

For any future batch, report:

- Records added or replaced.
- Files changed.
- Backups created or preserved.
- Candidate rejections or retries.
- Final counts and category distribution.
- Confirmation that stems, metadata references, and JPEG readability passed.
