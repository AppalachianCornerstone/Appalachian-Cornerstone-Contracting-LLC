from pathlib import Path
import json

folder = Path("assets/projects")
folder.mkdir(parents=True, exist_ok=True)
image_types = {".jpg", ".jpeg", ".png", ".webp"}
projects = []

for image in sorted(folder.iterdir(), key=lambda item: item.name.lower()):
    if not image.is_file() or image.suffix.lower() not in image_types:
        continue
    projects.append({
        "src": image.as_posix(),
        "alt": "Residential construction project by Appalachian Cornerstone Contracting",
    })

(folder / "gallery.json").write_text(
    json.dumps(projects, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
