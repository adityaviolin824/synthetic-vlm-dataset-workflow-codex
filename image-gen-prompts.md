# Image Generation Prompts

## Purpose

This file stores one realistic image generation prompt for each dataset image.

Each prompt is tied to an existing filename from `data/metadata.csv`.

The generated realistic image must later replace the placeholder image with the same filename.

Do not change filenames unless explicitly asked.

## Global Image Requirements

All generated images should follow these requirements:

- Photorealistic field inspection photo.
- Looks like a normal phone camera photo.
- Institutional building setting.
- No people.
- No faces.
- No readable private text.
- No brand logos.
- No text overlays.
- No labels.
- No arrows.
- No bounding boxes.
- No red circles.
- No watermarks.
- No extreme disaster damage.
- Defects should look realistic and physically plausible.
- Show enough surrounding context for inspection validation.
- Avoid close-up-only images unless the category clearly requires it.
- Use natural indoor or outdoor lighting according to the scene.
- Keep the image useful for later visual inspection validation.

## Responsible Prompting

- Describe observable visual conditions only.
- Do not infer hidden causes, ownership, funding, blame, or neglect.
- Avoid stereotypes, socioeconomic judgments, and sensationalized damage.
- Do not imply that a synthetic scene depicts a real institution or location.
- Keep issue severity aligned with the matching metadata and inspector comment.

## Negative Instructions

Avoid:

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

---

## Prompts

### 1. `classroom_001.jpg`

**Category:** `classroom`

**Scenario type:** `normal_no_issue`

**Issue present:** `false`

**Issue type:** `none`

**Issue summary:** `No visible issues.`

**Comment file:** `classroom_001.txt`

**Existing inspector comment:**

```text
The area appears generally clean and serviceable. No obvious defects are visible in this view.
```

**Image generation prompt:**

Photorealistic field inspection photo of a clean, serviceable classroom in an institutional building.

Scene:
A wide phone-camera view from the rear corner showing orderly desks, chairs, a plain teaching wall, windows, and a clear aisle. Surfaces are intact and the room has ordinary daylight.

Inspection condition:
The classroom is usable and tidy, with no obvious visible defects, damage, stains, or obstructions.

Visual requirements:
- Normal phone-camera photo
- Natural lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** generated

### 2. `classroom_002.jpg`

**Category:** `classroom`

**Scenario type:** `minor_issue`

**Issue present:** `true`

**Issue type:** `clutter`

**Issue summary:** `Minor clutter is visible.`

**Comment file:** `classroom_002.txt`

**Existing inspector comment:**

```text
Minor clutter is visible in the area. Access remains mostly open.
```

**Image generation prompt:**

Photorealistic field inspection photo of a classroom in an institutional building with mild clutter.

Scene:
A normal phone-camera view across desks and a mostly clear central aisle. A few empty cardboard boxes and stacked spare chairs sit near one side wall without blocking the main route.

Inspection condition:
Minor clutter is visible but access remains mostly open. The issue should look mild, realistic, and suitable for routine housekeeping attention.

Visual requirements:
- Normal phone-camera photo
- Natural lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** generated

### 3. `classroom_003.jpg`

**Category:** `classroom`

**Scenario type:** `moderate_issue`

**Issue present:** `true`

**Issue type:** `poor_lighting`

**Issue summary:** `The area appears dimly lit.`

**Comment file:** `classroom_003.txt`

**Existing inspector comment:**

```text
The area appears dimly lit. Visibility is limited in this view.
```

**Image generation prompt:**

Photorealistic field inspection photo of a dimly lit classroom in an institutional building.

Scene:
A wide phone-camera view showing desks, chairs, a teaching wall, and windows with blinds partly closed. Only a few ceiling lights are working, leaving the rear and side areas noticeably dim.

Inspection condition:
Poor lighting is clearly visible and limits visibility across part of the classroom, while the room remains realistic and usable.

Visual requirements:
- Normal phone-camera photo
- Realistic low indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** generated

### 4. `washroom_001.jpg`

**Category:** `washroom`

**Scenario type:** `normal_no_issue`

**Issue present:** `false`

**Issue type:** `none`

**Issue summary:** `No visible issues.`

**Comment file:** `washroom_001.txt`

**Existing inspector comment:**

```text
The area appears generally clean and serviceable. No obvious defects are visible in this view.
```

**Image generation prompt:**

Photorealistic field inspection photo of a clean institutional washroom.

Scene:
A normal phone-camera view showing intact tiled walls and floor, sinks, mirrors without readable reflections, and closed cubicle doors. The area is dry, orderly, and evenly lit.

Inspection condition:
The washroom appears clean, usable, and serviceable with no obvious visible defects, stains, broken fixtures, or damaged tiles.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 5. `washroom_002.jpg`

**Category:** `washroom`

**Scenario type:** `minor_issue`

**Issue present:** `true`

**Issue type:** `water_stain`

**Issue summary:** `Visible staining is present.`

**Comment file:** `washroom_002.txt`

**Existing inspector comment:**

```text
A visible stain appears on the surface. The affected area should be checked during routine maintenance.
```

**Image generation prompt:**

Photorealistic field inspection photo of an institutional washroom with a mild water stain.

Scene:
A phone-camera view showing sinks, tiled floor, and the lower section of a painted wall near a plumbing area. A small pale brown water stain is visible on the wall while the surrounding washroom remains clean and usable.

Inspection condition:
The water stain is visible but mild, localized, and physically plausible, with no active flooding or severe damage.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 6. `washroom_003.jpg`

**Category:** `washroom`

**Scenario type:** `moderate_issue`

**Issue present:** `true`

**Issue type:** `broken_tile`

**Issue summary:** `Damaged tile is visible.`

**Comment file:** `washroom_003.txt`

**Existing inspector comment:**

```text
One or more tiles appear damaged. The surface is uneven in that section.
```

**Image generation prompt:**

Photorealistic field inspection photo of an institutional washroom with damaged floor tiles.

Scene:
A normal phone-camera view showing part of the washroom floor, sinks, and cubicle entrances. Two adjacent floor tiles near the walkway are cracked and one edge is slightly raised, making the surface uneven.

Inspection condition:
The broken tiles are clearly visible and moderately concerning but localized, realistic, and without extreme destruction.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 7. `staircase_001.jpg`

**Category:** `staircase`

**Scenario type:** `normal_no_issue`

**Issue present:** `false`

**Issue type:** `none`

**Issue summary:** `No visible issues.`

**Comment file:** `staircase_001.txt`

**Existing inspector comment:**

```text
The area appears generally clean and serviceable. No obvious defects are visible in this view.
```

**Image generation prompt:**

Photorealistic field inspection photo of a clean institutional staircase.

Scene:
A phone-camera view from a landing showing intact steps, secure metal handrails, plain painted walls, and a clear route between floors. Lighting is ordinary and even.

Inspection condition:
The staircase appears clean, usable, and serviceable with no obvious visible defects, obstructions, or damaged railings.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 8. `staircase_002.jpg`

**Category:** `staircase`

**Scenario type:** `minor_issue`

**Issue present:** `true`

**Issue type:** `poor_lighting`

**Issue summary:** `The area appears dimly lit.`

**Comment file:** `staircase_002.txt`

**Existing inspector comment:**

```text
The area appears dimly lit. Visibility is limited in this view.
```

**Image generation prompt:**

Photorealistic field inspection photo of a slightly dim institutional staircase.

Scene:
A normal phone-camera view from the lower landing showing intact steps and handrails. One ceiling fixture is not illuminated, leaving a mild shadow across part of the upper flight.

Inspection condition:
Poor lighting is visible but mild. Visibility is somewhat limited in one section while the staircase remains recognizable and usable.

Visual requirements:
- Normal phone-camera photo
- Realistic low indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 9. `staircase_003.jpg`

**Category:** `staircase`

**Scenario type:** `moderate_issue`

**Issue present:** `true`

**Issue type:** `damaged_railing`

**Issue summary:** `A railing section appears damaged.`

**Comment file:** `staircase_003.txt`

**Existing inspector comment:**

```text
A section of the railing appears damaged. The edge area should be checked.
```

**Image generation prompt:**

Photorealistic field inspection photo of an institutional staircase with a damaged railing section.

Scene:
A phone-camera view from a landing showing the stair flight and surrounding walls. One short section of the metal railing is visibly bent and slightly detached at a mounting point, while the rest remains intact.

Inspection condition:
The railing damage is clearly visible and moderately concerning but localized, physically plausible, and not catastrophic.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 10. `corridor_001.jpg`

**Category:** `corridor`

**Scenario type:** `normal_no_issue`

**Issue present:** `false`

**Issue type:** `none`

**Issue summary:** `No visible issues.`

**Comment file:** `corridor_001.txt`

**Existing inspector comment:**

```text
The area appears generally clean and serviceable. No obvious defects are visible in this view.
```

**Image generation prompt:**

Photorealistic field inspection photo of a clean institutional corridor.

Scene:
A centered phone-camera view down a plain corridor with intact floor finish, closed doors, clean walls, and a fully clear walking route. Ordinary ceiling lights provide even illumination.

Inspection condition:
The corridor appears clean, usable, and serviceable with no obvious visible defects, dirt, or obstructions.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 11. `corridor_002.jpg`

**Category:** `corridor`

**Scenario type:** `minor_issue`

**Issue present:** `true`

**Issue type:** `dirty_floor`

**Issue summary:** `The floor has visible dirt marks.`

**Comment file:** `corridor_002.txt`

**Existing inspector comment:**

```text
The floor shows visible dirt and marks. Cleaning would improve the area's appearance.
```

**Image generation prompt:**

Photorealistic field inspection photo of an institutional corridor with a mildly dirty floor.

Scene:
A normal phone-camera view down a mostly clear corridor. Light shoe marks, dusty streaks, and a few small dirt patches are visible on part of the floor, while walls and doors remain intact.

Inspection condition:
The dirt marks are visible but mild and realistic, indicating routine cleaning is needed without suggesting damage.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 12. `corridor_003.jpg`

**Category:** `corridor`

**Scenario type:** `moderate_issue`

**Issue present:** `true`

**Issue type:** `blocked_corridor`

**Issue summary:** `Part of the corridor is obstructed.`

**Comment file:** `corridor_003.txt`

**Existing inspector comment:**

```text
Part of the corridor is visibly obstructed. The passageway should be cleared.
```

**Image generation prompt:**

Photorealistic field inspection photo of a partially obstructed institutional corridor.

Scene:
A phone-camera view down the corridor showing several stacked empty boxes and two spare chairs extending from one wall into the walking route. A narrower path remains open around the obstruction.

Inspection condition:
The corridor is clearly and moderately obstructed, but the scene remains realistic and does not show extreme blockage or disaster damage.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 13. `electrical_panel_001.jpg`

**Category:** `electrical_panel`

**Scenario type:** `normal_no_issue`

**Issue present:** `false`

**Issue type:** `none`

**Issue summary:** `No visible issues.`

**Comment file:** `electrical_panel_001.txt`

**Existing inspector comment:**

```text
The area appears generally clean and serviceable. No obvious defects are visible in this view.
```

**Image generation prompt:**

Photorealistic field inspection photo of a serviceable electrical panel area in an institutional building.

Scene:
A normal phone-camera view showing a closed, intact metal electrical panel mounted on a clean utility-room wall. The floor area in front is clear and no readable labels are visible.

Inspection condition:
The panel and surrounding area appear clean, accessible, and serviceable with no obvious visible defects, corrosion, exposed wiring, or obstructions.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 14. `electrical_panel_002.jpg`

**Category:** `electrical_panel`

**Scenario type:** `minor_issue`

**Issue present:** `true`

**Issue type:** `rust_mark`

**Issue summary:** `Rust staining is visible.`

**Comment file:** `electrical_panel_002.txt`

**Existing inspector comment:**

```text
Rust staining is visible on the surface. The affected area looks weathered.
```

**Image generation prompt:**

Photorealistic field inspection photo of an institutional electrical panel with minor rust staining.

Scene:
A phone-camera view of a closed metal electrical panel and its surrounding utility wall. A small localized rust streak is visible near the panel's lower edge, while the enclosure remains closed and intact.

Inspection condition:
The rust staining is mild, visible, and physically plausible, with no exposed wiring or severe corrosion.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 15. `electrical_panel_003.jpg`

**Category:** `electrical_panel`

**Scenario type:** `moderate_issue`

**Issue present:** `true`

**Issue type:** `unsafe_electrical_panel`

**Issue summary:** `The electrical panel area is exposed.`

**Comment file:** `electrical_panel_003.txt`

**Existing inspector comment:**

```text
The electrical panel area appears exposed and needs attention. Access around the panel should stay clear.
```

**Image generation prompt:**

Photorealistic field inspection photo of an unsafe electrical panel area in an institutional building.

Scene:
A normal phone-camera view of a utility-room wall where an electrical panel door is partly open, revealing a limited view of internal breakers and neatly routed wiring. The floor area remains clear and the scene contains no readable labels.

Inspection condition:
The exposed panel condition is clearly visible and moderately unsafe, but realistic, localized, and without sparks, fire, or extreme damage.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage, sparks, flames

**Replacement status:** pending

### 16. `ceiling_001.jpg`

**Category:** `ceiling`

**Scenario type:** `normal_no_issue`

**Issue present:** `false`

**Issue type:** `none`

**Issue summary:** `No visible issues.`

**Comment file:** `ceiling_001.txt`

**Existing inspector comment:**

```text
The area appears generally clean and serviceable. No obvious defects are visible in this view.
```

**Image generation prompt:**

Photorealistic field inspection photo of an intact institutional building ceiling.

Scene:
An upward-angled phone-camera view showing a clean painted ceiling, intact ceiling joints, simple light fixtures, and the upper portions of surrounding walls for context.

Inspection condition:
The ceiling appears clean and serviceable with no obvious visible cracks, stains, damp patches, or damaged plaster.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 17. `ceiling_002.jpg`

**Category:** `ceiling`

**Scenario type:** `minor_issue`

**Issue present:** `true`

**Issue type:** `water_stain`

**Issue summary:** `Visible staining is present.`

**Comment file:** `ceiling_002.txt`

**Existing inspector comment:**

```text
A visible stain appears on the surface. The affected area should be checked during routine maintenance.
```

**Image generation prompt:**

Photorealistic field inspection photo of an institutional ceiling with a mild water stain.

Scene:
An upward-angled phone-camera view showing a painted ceiling, nearby light fixture, and upper wall edges. A small pale brown irregular stain is visible away from the fixture.

Inspection condition:
The water stain is visible but mild and localized, with the ceiling surface otherwise intact and no active dripping.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 18. `ceiling_003.jpg`

**Category:** `ceiling`

**Scenario type:** `moderate_issue`

**Issue present:** `true`

**Issue type:** `ceiling_crack`

**Issue summary:** `A crack is visible on the ceiling.`

**Comment file:** `ceiling_003.txt`

**Existing inspector comment:**

```text
A crack is visible along the ceiling surface. The area should be monitored for further change.
```

**Image generation prompt:**

Photorealistic field inspection photo of an institutional ceiling with a visible crack.

Scene:
An upward-angled phone-camera view showing a painted ceiling, part of a light fixture, and upper wall edges. A thin but clearly visible branching crack runs across a section of the ceiling surface.

Inspection condition:
The ceiling crack is moderately noticeable and physically plausible, with no collapse, exposed structure, or extreme damage.

Visual requirements:
- Normal phone-camera photo
- Natural indoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 19. `exterior_wall_001.jpg`

**Category:** `exterior_wall`

**Scenario type:** `normal_no_issue`

**Issue present:** `false`

**Issue type:** `none`

**Issue summary:** `No visible issues.`

**Comment file:** `exterior_wall_001.txt`

**Existing inspector comment:**

```text
The area appears generally clean and serviceable. No obvious defects are visible in this view.
```

**Image generation prompt:**

Photorealistic field inspection photo of an intact exterior wall of an institutional building.

Scene:
A normal phone-camera view showing a broad section of painted masonry wall, one plain window, the wall base, and a small amount of surrounding pavement and landscaping.

Inspection condition:
The exterior wall appears clean and serviceable with no obvious visible cracks, damp patches, peeling paint, or damaged plaster.

Visual requirements:
- Normal phone-camera photo
- Natural outdoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 20. `exterior_wall_002.jpg`

**Category:** `exterior_wall`

**Scenario type:** `minor_issue`

**Issue present:** `true`

**Issue type:** `damp_patch`

**Issue summary:** `A damp patch is visible on the wall.`

**Comment file:** `exterior_wall_002.txt`

**Existing inspector comment:**

```text
A dark patch is visible on the wall surface. The finish in that area looks affected.
```

**Image generation prompt:**

Photorealistic field inspection photo of an institutional exterior wall with a mild damp patch.

Scene:
A phone-camera view showing a painted masonry wall, its base, nearby pavement, and part of a plain window. A localized dark damp patch is visible near the lower wall surface.

Inspection condition:
The damp patch is mild, visible, and physically plausible, affecting only a limited area of the finish without severe deterioration.

Visual requirements:
- Normal phone-camera photo
- Natural outdoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending

### 21. `exterior_wall_003.jpg`

**Category:** `exterior_wall`

**Scenario type:** `moderate_issue`

**Issue present:** `true`

**Issue type:** `wall_crack`

**Issue summary:** `A crack is visible on the wall.`

**Comment file:** `exterior_wall_003.txt`

**Existing inspector comment:**

```text
A crack is visible on the wall surface. The finish in that area should be monitored.
```

**Image generation prompt:**

Photorealistic field inspection photo of an institutional exterior wall with a visible crack.

Scene:
A normal phone-camera view showing a broad section of painted masonry wall, a plain window edge, wall base, and surrounding pavement. A clear vertical-to-diagonal crack runs through a limited section of the painted finish.

Inspection condition:
The wall crack is moderately visible and physically plausible, with localized finish damage but no structural collapse or extreme destruction.

Visual requirements:
- Normal phone-camera photo
- Natural outdoor lighting
- No people
- No faces
- No readable private text
- No brand logos
- No text overlays, labels, arrows, bounding boxes, or red circles
- Defect should be visible but not exaggerated
- Show enough surrounding context for inspection validation

**Negative instructions:**

cartoon, illustration, 3d render, anime, cinematic lighting, dramatic lighting, people, faces, text overlay, labels, arrows, bounding boxes, red circles, watermark, logo, readable document, private information, unrealistic destruction, disaster scene, exaggerated damage

**Replacement status:** pending
