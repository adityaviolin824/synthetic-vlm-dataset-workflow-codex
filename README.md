# Synthetic Image-Text Dataset Workflow for VLM Experiments

This repository documents a small workflow I used to create a synthetic image-text dataset for Visual Language Model experiments.

I made this after trying a few different ways to organize generated images, comments, prompts, and metadata. The main problem I wanted to solve was simple:

How do I create a small synthetic dataset where every image, text comment, and metadata row stays aligned and easy to verify?

This is not meant to be a framework, benchmark, or production dataset. It is just a practical workflow that worked for me, shared in case someone else is trying to build something similar.

All included images are synthetic. They should not be presented as evidence from a real inspection, real institution, real organization, or real location.

## What This Repository Contains

The repository contains:

* Synthetic JPEG images.
* Matching plain-text comments.
* A metadata CSV file.
* A local placeholder image generator.
* Prompt inventories used for image generation.
* A simple plan for adding or replacing records safely.

The main idea is that every record has three linked parts:

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

The filename stem, such as `washroom_001`, is treated as the stable identity for the record.

## Current Dataset Snapshot

| Artifact               | Count |
| ---------------------- | ----: |
| JPEG images            |    27 |
| Matching text comments |    27 |
| Metadata rows          |    27 |
| Categories             |     8 |

Current category distribution:

| Category          | Records |
| ----------------- | ------: |
| classroom         |       3 |
| washroom          |       7 |
| staircase         |       3 |
| corridor          |       3 |
| electrical_panel  |       3 |
| ceiling           |       3 |
| exterior_wall     |       3 |
| fire_extinguisher |       2 |

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

## Key Files

* `AGENTS.md` contains the rules I wanted Codex to follow while working in the repository.
* `PLAN.md` contains the step-by-step process I followed.
* `scripts/generate_sample_dataset.py` creates a small local placeholder dataset using Python and Pillow.
* `image-gen-prompts.md` contains a generic prompt inventory.
* `image-gen-prompts-indian-ngo-school.md` is an example of adapting the same records to a specific visual context.
* `data/metadata.csv` connects each image to its category, scenario, issue label, summary, and comment file.
* `data/sample_images/` contains the synthetic images.
* `data/sample_comments/` contains matching text observations.
* `data/placeholder_image_backup/` stores earlier placeholder versions.

## Metadata Format

`data/metadata.csv` uses this column order:

```text
filename,category,scenario_type,issue_present,issue_type,issue_summary,comment_file
```

The comments are intentionally short and plain. They describe visible details only. They avoid confidence scores, model-like wording, and hidden-cause assumptions.

Example comment:

```text
A visible stain appears on the surface. The affected area should be checked during routine maintenance.
```

## Workflow I Followed

### 1. Define the dataset contract first

Before generating anything, I wrote down the folder structure, metadata columns, naming rules, and constraints.

This helped avoid messy mismatches later.

The important rule was:

```text
image filename stem == comment filename stem == metadata identity
```

### 2. Create simple local placeholders

I first generated simple placeholder images locally using Python and Pillow.

These placeholder images were not meant to be realistic. Their purpose was only to test the structure:

* Are the image files created correctly?
* Are the comment files created correctly?
* Does every image have a matching comment?
* Does the metadata match the files?
* Can the dataset be verified before realistic images are added?

The generator supports:

```bash
uv run python scripts/generate_sample_dataset.py --count-per-category 1
uv run python scripts/generate_sample_dataset.py --count-per-category 3
uv run python scripts/generate_sample_dataset.py --count-per-category 3 --dry-run
uv run python scripts/generate_sample_dataset.py --count-per-category 3 --force
```

The dry run was useful because it showed planned files and metadata before writing anything.

### 3. Create one prompt per image

After the placeholder dataset was stable, I created a prompt inventory.

Each image got its own prompt section containing:

* Filename.
* Category.
* Scenario type.
* Issue type.
* Issue summary.
* Matching comment.
* Image generation prompt.
* Negative instructions.
* Replacement status.

This made it easier to review prompts before generating images.

### 4. Replace images slowly

Instead of replacing everything at once, I worked in small batches.

The process was:

1. Pick a small group of images.
2. Back up the placeholders.
3. Generate realistic candidates.
4. Manually inspect the results.
5. Reject anything with issues like readable text, wrong setting, people, logos, or mismatched defects.
6. Save accepted images using the exact same filename.
7. Verify the dataset again.

This part mattered more than I expected. A prompt can look fine and still produce an image with some unwanted detail.

### 5. Verify after changes

After adding or replacing images, I checked:

* Image count.
* Comment count.
* Metadata row count.
* Matching filename stems.
* Missing files.
* Duplicate filenames.
* Readable JPEG files.
* Whether comments and labels still matched the visible image.

This made the dataset easier to trust, even though it is still synthetic and small.

## Why I Kept Placeholder and Prompt Files

The placeholder generator is useful because it gives a deterministic starting point.

The prompt inventories are useful because they preserve the reasoning behind the generated images.

Together, they make the dataset easier to inspect and modify later.

## Requirements

* Python 3.10 or newer.
* `uv` for local Python dependency management.
* Pillow for local placeholder generation.

Install Pillow with:

```bash
uv add pillow
```

Run a dry run:

```bash
uv run python scripts/generate_sample_dataset.py --count-per-category 1 --dry-run
```

Generate the local placeholder baseline:

```bash
uv run python scripts/generate_sample_dataset.py --count-per-category 3
```

Be careful with:

```bash
uv run python scripts/generate_sample_dataset.py --count-per-category 3 --force
```

It can overwrite curated images with placeholder images.

## Possible Use Cases

This workflow may be useful if you are experimenting with:

* Small image-text datasets.
* VLM proof-of-concept projects.
* Prompt-based synthetic data creation.
* Image and text metadata alignment.
* Human review workflows for generated images.
* Dataset verification before VLM testing.

## Limitations

This repository has important limitations:

* The dataset is small.
* The images are synthetic.
* The labels are not expert-certified.
* The dataset should not be used as a real benchmark.
* The images do not represent any real location, organization, or inspection site.
* Visual realism may vary across images.
* There is no VLM inference pipeline included.
* There is no training or evaluation pipeline included.

This is mostly a workflow example.

## Responsible Use Notes

Please do not use these images as real-world evidence.

For synthetic datasets like this, I think it is important to:

* Clearly label generated images as synthetic.
* Avoid identifiable people or faces.
* Avoid private text, logos, or sensitive details.
* Avoid exaggerated or stereotyped scenes.
* Review generated images manually.
* Keep prompts and metadata available for traceability.
* Treat labels as reviewed annotations, not ground truth from real inspections.

## Final Note

This was a small experiment in making synthetic image-text data more organized and auditable.

The main thing I found useful was not the image generation itself. It was the discipline of keeping filenames, comments, prompts, and metadata aligned from the beginning.
