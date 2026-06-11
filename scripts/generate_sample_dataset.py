#!/usr/bin/env python3
"""Generate a small local sample dataset for field inspection images."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
IMAGE_DIR = DATA_DIR / "sample_images"
COMMENT_DIR = DATA_DIR / "sample_comments"
METADATA_PATH = DATA_DIR / "metadata.csv"

MAX_COUNT_PER_CATEGORY = 3

CATEGORIES = [
    "classroom",
    "washroom",
    "staircase",
    "corridor",
    "electrical_panel",
    "ceiling",
    "exterior_wall",
]

SCENARIO_ORDER = [
    "normal_no_issue",
    "minor_issue",
    "moderate_issue",
]

CATEGORY_ISSUES = {
    "classroom": {
        "minor_issue": "clutter",
        "moderate_issue": "poor_lighting",
    },
    "washroom": {
        "minor_issue": "water_stain",
        "moderate_issue": "broken_tile",
    },
    "staircase": {
        "minor_issue": "poor_lighting",
        "moderate_issue": "damaged_railing",
    },
    "corridor": {
        "minor_issue": "dirty_floor",
        "moderate_issue": "blocked_corridor",
    },
    "electrical_panel": {
        "minor_issue": "rust_mark",
        "moderate_issue": "unsafe_electrical_panel",
    },
    "ceiling": {
        "minor_issue": "water_stain",
        "moderate_issue": "ceiling_crack",
    },
    "exterior_wall": {
        "minor_issue": "damp_patch",
        "moderate_issue": "wall_crack",
    },
}

ISSUE_SUMMARIES = {
    "none": "No visible issues.",
    "clutter": "Minor clutter is visible.",
    "water_stain": "Visible staining is present.",
    "poor_lighting": "The area appears dimly lit.",
    "broken_tile": "Damaged tile is visible.",
    "damaged_railing": "A railing section appears damaged.",
    "dirty_floor": "The floor has visible dirt marks.",
    "blocked_corridor": "Part of the corridor is obstructed.",
    "rust_mark": "Rust staining is visible.",
    "unsafe_electrical_panel": "The electrical panel area is exposed.",
    "ceiling_crack": "A crack is visible on the ceiling.",
    "damp_patch": "A damp patch is visible on the wall.",
    "wall_crack": "A crack is visible on the wall.",
    "damaged_plaster": "The wall finish shows visible damage.",
}

COMMENT_TEXT = {
    "none": (
        "The area appears generally clean and serviceable. "
        "No obvious defects are visible in this view."
    ),
    "clutter": (
        "Minor clutter is visible in the area. "
        "Access remains mostly open."
    ),
    "water_stain": (
        "A visible stain appears on the surface. "
        "The affected area should be checked during routine maintenance."
    ),
    "poor_lighting": (
        "The area appears dimly lit. "
        "Visibility is limited in this view."
    ),
    "broken_tile": (
        "One or more tiles appear damaged. "
        "The surface is uneven in that section."
    ),
    "damaged_railing": (
        "A section of the railing appears damaged. "
        "The edge area should be checked."
    ),
    "dirty_floor": (
        "The floor shows visible dirt and marks. "
        "Cleaning would improve the area's appearance."
    ),
    "blocked_corridor": (
        "Part of the corridor is visibly obstructed. "
        "The passageway should be cleared."
    ),
    "rust_mark": (
        "Rust staining is visible on the surface. "
        "The affected area looks weathered."
    ),
    "unsafe_electrical_panel": (
        "The electrical panel area appears exposed and needs attention. "
        "Access around the panel should stay clear."
    ),
    "ceiling_crack": (
        "A crack is visible along the ceiling surface. "
        "The area should be monitored for further change."
    ),
    "damp_patch": (
        "A dark patch is visible on the wall surface. "
        "The finish in that area looks affected."
    ),
    "wall_crack": (
        "A crack is visible on the wall surface. "
        "The finish in that area should be monitored."
    ),
}


@dataclass(frozen=True)
class PlannedRecord:
    image_path: Path
    comment_path: Path
    metadata_row: dict[str, str]
    scenario_type: str
    issue_type: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a small local sample dataset for inspection images."
    )
    parser.add_argument(
        "--count-per-category",
        type=int,
        default=1,
        help="Number of samples to generate per category (1-3).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned files and metadata without creating anything.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing generated files if they already exist.",
    )
    args = parser.parse_args()
    if args.count_per_category < 1:
        parser.error("--count-per-category must be at least 1")
    if args.count_per_category > MAX_COUNT_PER_CATEGORY:
        parser.error("--count-per-category must be 3 or less")
    return args


def build_plan(count_per_category: int) -> list[PlannedRecord]:
    records: list[PlannedRecord] = []
    for category in CATEGORIES:
        for index in range(count_per_category):
            scenario_type = SCENARIO_ORDER[index]
            issue_type = issue_type_for(category, scenario_type)
            stem = f"{category}_{index + 1:03d}"
            image_path = IMAGE_DIR / f"{stem}.jpg"
            comment_path = COMMENT_DIR / f"{stem}.txt"
            metadata_row = {
                "filename": image_path.name,
                "category": category,
                "scenario_type": scenario_type,
                "issue_present": "false" if issue_type == "none" else "true",
                "issue_type": issue_type,
                "issue_summary": ISSUE_SUMMARIES[issue_type],
                "comment_file": comment_path.name,
            }
            records.append(
                PlannedRecord(
                    image_path=image_path,
                    comment_path=comment_path,
                    metadata_row=metadata_row,
                    scenario_type=scenario_type,
                    issue_type=issue_type,
                )
            )
    return records


def issue_type_for(category: str, scenario_type: str) -> str:
    if scenario_type == "normal_no_issue":
        return "none"
    return CATEGORY_ISSUES[category][scenario_type]


def ensure_no_overwrites(records: Iterable[PlannedRecord]) -> None:
    existing_paths = [path for record in records for path in (record.image_path, record.comment_path) if path.exists()]
    if METADATA_PATH.exists():
        existing_paths.append(METADATA_PATH)
    if existing_paths:
        unique_paths = sorted({str(path) for path in existing_paths})
        message = [
            "Refusing to overwrite existing generated files.",
            "Re-run with --force to replace them.",
            "Existing paths:",
            *[f"  - {path}" for path in unique_paths],
        ]
        raise SystemExit("\n".join(message))


def print_dry_run(records: Iterable[PlannedRecord]) -> None:
    print("Dry run plan")
    print("Images")
    for record in records:
        print(f"  - {record.image_path}")
    print("Comments")
    for record in records:
        print(f"  - {record.comment_path}")
    print("Metadata rows")
    print(",".join(["filename", "category", "scenario_type", "issue_present", "issue_type", "issue_summary", "comment_file"]))
    for record in records:
        row = record.metadata_row
        print(
            ",".join(
                [
                    row["filename"],
                    row["category"],
                    row["scenario_type"],
                    row["issue_present"],
                    row["issue_type"],
                    row["issue_summary"],
                    row["comment_file"],
                ]
            )
        )
    print("Dry run complete. No files were created.")


def write_dataset(records: Iterable[PlannedRecord], force: bool) -> None:
    try:
        from PIL import Image, ImageDraw
    except ImportError as exc:
        raise SystemExit(
            "Pillow is required for real dataset generation. Install it with "
            "'uv add pillow' or your preferred local package manager, then rerun."
        ) from exc

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    COMMENT_DIR.mkdir(parents=True, exist_ok=True)

    if not force:
        ensure_no_overwrites(records)

    written_images = 0
    written_comments = 0
    metadata_rows: list[dict[str, str]] = []

    for record in records:
        comment_text = COMMENT_TEXT[record.issue_type]
        metadata_rows.append(record.metadata_row)

        if force or not record.image_path.exists():
            create_placeholder_image(Image, ImageDraw, record)
            written_images += 1
            print(f"Generated image: {record.image_path}")

        if force or not record.comment_path.exists():
            record.comment_path.write_text(comment_text + "\n", encoding="utf-8")
            written_comments += 1
            print(f"Generated comment: {record.comment_path}")

    with METADATA_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "filename",
                "category",
                "scenario_type",
                "issue_present",
                "issue_type",
                "issue_summary",
                "comment_file",
            ],
        )
        writer.writeheader()
        writer.writerows(metadata_rows)
    print(f"Generated metadata: {METADATA_PATH}")

    verify_dataset(records, metadata_rows, written_images, written_comments)


def create_placeholder_image(image_module, draw_module, record: PlannedRecord) -> None:
    width = 960
    height = 640
    scenario_type = record.scenario_type
    issue_type = record.issue_type
    category = record.metadata_row["category"]

    base_colors = {
        "classroom": (231, 238, 247),
        "washroom": (235, 243, 240),
        "staircase": (238, 236, 230),
        "corridor": (234, 234, 238),
        "electrical_panel": (241, 236, 228),
        "ceiling": (242, 242, 236),
        "exterior_wall": (229, 233, 236),
    }
    image = image_module.new("RGB", (width, height), base_colors[category])
    draw = draw_module.Draw(image)

    if category == "classroom":
        draw_classroom(draw, width, height)
    elif category == "washroom":
        draw_washroom(draw, width, height)
    elif category == "staircase":
        draw_staircase(draw, width, height)
    elif category == "corridor":
        draw_corridor(draw, width, height)
    elif category == "electrical_panel":
        draw_electrical_panel(draw, width, height)
    elif category == "ceiling":
        draw_ceiling(draw, width, height)
    elif category == "exterior_wall":
        draw_exterior_wall(draw, width, height)

    apply_issue_overlay(draw, category, scenario_type, issue_type, width, height)
    image.save(record.image_path, format="JPEG", quality=88)


def draw_classroom(draw, width: int, height: int) -> None:
    draw.rectangle((0, height * 0.65, width, height), fill=(210, 219, 228))
    for x in range(100, width - 100, 180):
        draw.rectangle((x, 240, x + 120, 360), outline=(150, 150, 150), width=3, fill=(244, 244, 236))
        draw.line((x + 60, 360, x + 60, 460), fill=(120, 120, 120), width=4)
    draw.rectangle((70, 90, 260, 210), outline=(120, 120, 130), width=4, fill=(245, 248, 250))
    draw.rectangle((320, 100, 430, 260), outline=(130, 120, 110), width=4, fill=(230, 220, 200))
    draw.line((0, 220, width, 220), fill=(170, 177, 184), width=3)


def draw_washroom(draw, width: int, height: int) -> None:
    draw.rectangle((0, 0, width, height), fill=(232, 243, 241))
    for y in range(80, height, 90):
        draw.line((0, y, width, y), fill=(196, 210, 206), width=3)
    for x in range(80, width, 120):
        draw.line((x, 0, x, height), fill=(196, 210, 206), width=3)
    draw.ellipse((100, 170, 240, 360), outline=(120, 120, 120), width=5, fill=(250, 250, 250))
    draw.rounded_rectangle((360, 140, 610, 420), radius=16, outline=(120, 120, 120), width=5, fill=(240, 240, 240))
    draw.rectangle((700, 120, 860, 280), outline=(100, 120, 130), width=4, fill=(226, 236, 238))


def draw_staircase(draw, width: int, height: int) -> None:
    draw.polygon([(0, height), (width, height), (width, 390), (0, 260)], fill=(215, 215, 210))
    step_top = 350
    for step in range(5):
        offset = step * 95
        draw.polygon(
            [
                (120 + offset, step_top - step * 50),
                (240 + offset, step_top - step * 50),
                (210 + offset, step_top - step * 50 + 50),
                (90 + offset, step_top - step * 50 + 50),
            ],
            outline=(140, 140, 140),
            fill=(235, 235, 230),
        )
    draw.line((80, 330, 780, 120), fill=(115, 115, 115), width=8)
    draw.line((95, 325, 95, 580), fill=(105, 105, 105), width=7)


def draw_corridor(draw, width: int, height: int) -> None:
    draw.rectangle((0, 0, width, height), fill=(233, 236, 240))
    draw.rectangle((0, 430, width, height), fill=(212, 214, 218))
    draw.line((140, 0, 240, 430), fill=(185, 190, 196), width=6)
    draw.line((820, 0, 700, 430), fill=(185, 190, 196), width=6)
    draw.rectangle((160, 160, 320, 420), outline=(145, 145, 150), width=4, fill=(244, 244, 242))
    draw.rectangle((640, 160, 800, 420), outline=(145, 145, 150), width=4, fill=(244, 244, 242))


def draw_electrical_panel(draw, width: int, height: int) -> None:
    draw.rectangle((0, 0, width, height), fill=(238, 232, 224))
    draw.rectangle((290, 120, 670, 520), outline=(80, 80, 80), width=7, fill=(210, 214, 220))
    for x in range(330, 640, 75):
        draw.rectangle((x, 170, x + 32, 380), outline=(90, 90, 100), width=3, fill=(235, 238, 242))
    draw.line((300, 560, 660, 560), fill=(160, 160, 160), width=4)


def draw_ceiling(draw, width: int, height: int) -> None:
    draw.rectangle((0, 0, width, height), fill=(244, 243, 235))
    draw.line((0, 140, width, 140), fill=(210, 207, 198), width=3)
    draw.line((0, 300, width, 300), fill=(210, 207, 198), width=3)
    draw.ellipse((380, 160, 580, 360), outline=(170, 170, 165), width=5, fill=(250, 250, 246))


def draw_exterior_wall(draw, width: int, height: int) -> None:
    draw.rectangle((0, 0, width, height), fill=(224, 229, 233))
    draw.rectangle((80, 90, 880, 540), outline=(170, 176, 180), width=5, fill=(236, 240, 242))
    draw.line((100, 170, 860, 160), fill=(198, 202, 206), width=4)
    draw.line((100, 320, 860, 310), fill=(198, 202, 206), width=4)
    draw.line((100, 470, 860, 460), fill=(198, 202, 206), width=4)


def apply_issue_overlay(
    draw,
    category: str,
    scenario_type: str,
    issue_type: str,
    width: int,
    height: int,
) -> None:
    if scenario_type == "normal_no_issue":
        return

    if issue_type == "clutter":
        draw.rectangle((90, 470, 220, 560), fill=(170, 145, 110))
        draw.rectangle((210, 495, 330, 590), fill=(155, 128, 104))
    elif issue_type == "water_stain":
        draw.ellipse((420, 60, 640, 190), fill=(184, 165, 125))
    elif issue_type == "poor_lighting":
        draw.rectangle((0, 0, width, height), fill=(180, 185, 190))
    elif issue_type == "broken_tile":
        draw.line((110, 520, 260, 470), fill=(125, 115, 110), width=6)
        draw.line((260, 470, 350, 560), fill=(125, 115, 110), width=6)
    elif issue_type == "damaged_railing":
        draw.line((130, 350, 780, 130), fill=(90, 70, 60), width=11)
        draw.line((300, 300, 300, 520), fill=(120, 100, 90), width=7)
    elif issue_type == "dirty_floor":
        draw.rectangle((0, 470, width, height), fill=(195, 188, 176))
    elif issue_type == "blocked_corridor":
        draw.rectangle((330, 320, 650, 560), fill=(156, 125, 98))
    elif issue_type == "rust_mark":
        draw.ellipse((350, 210, 460, 320), fill=(165, 105, 70))
    elif issue_type == "unsafe_electrical_panel":
        draw.rectangle((250, 90, 710, 540), outline=(220, 80, 60), width=8)
        draw.line((360, 180, 610, 480), fill=(220, 80, 60), width=7)
        draw.line((610, 180, 360, 480), fill=(220, 80, 60), width=7)
    elif issue_type == "ceiling_crack":
        draw.line((120, 120, 850, 170), fill=(120, 90, 80), width=5)
    elif issue_type == "damp_patch":
        draw.ellipse((300, 150, 580, 360), fill=(168, 183, 170))
    elif issue_type == "wall_crack":
        draw.line((180, 120, 330, 210), fill=(110, 90, 80), width=5)
        draw.line((330, 210, 500, 180), fill=(110, 90, 80), width=5)
    elif issue_type == "damaged_plaster":
        draw.rectangle((150, 170, 430, 410), fill=(200, 195, 184))


def verify_dataset(
    records: Iterable[PlannedRecord],
    metadata_rows: list[dict[str, str]],
    written_images: int,
    written_comments: int,
) -> None:
    record_list = list(records)
    if len(metadata_rows) != len(record_list):
        raise SystemExit("Metadata row count does not match the planned image count.")
    if written_images != len(record_list):
        raise SystemExit("Image count does not match the planned image count.")
    if written_comments != len(record_list):
        raise SystemExit("Comment count does not match the planned image count.")

    image_stems = {record.image_path.stem for record in record_list}
    comment_stems = {record.comment_path.stem for record in record_list}
    if image_stems != comment_stems:
        raise SystemExit("Every image must have a matching comment file stem.")


def main() -> int:
    args = parse_args()
    records = build_plan(args.count_per_category)

    if args.dry_run:
        print_dry_run(records)
        return 0

    write_dataset(records, args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
