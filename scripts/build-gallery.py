from pathlib import Path
import json
import re

folder = Path("assets/projects")
folder.mkdir(parents=True, exist_ok=True)
image_types = {".jpg", ".jpeg", ".png", ".webp"}
projects = []

for image in sorted(folder.iterdir(), key=lambda item: item.name.lower()):
    if not image.is_file() or image.suffix.lower() not in image_types:
        continue
    title = re.sub(r"[-_]+", " ", image.stem).strip().title()
    projects.append({
        "src": image.as_posix(),
        "title": title,
        "alt": f"{title} by Appalachian Cornerstone Contracting",
    })

(folder / "gallery.json").write_text(
    json.dumps(projects, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
