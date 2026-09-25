const gallery = document.querySelector("#project-gallery");
const emptyState = document.querySelector("#gallery-empty");

async function loadProjects() {
  if (!gallery || !emptyState) return;

  try {
    const response = await fetch("assets/projects/gallery.json");
    if (!response.ok) throw new Error("Gallery index unavailable");

    const projects = await response.json();
    if (!Array.isArray(projects) || projects.length === 0) return;

    emptyState.hidden = true;
    for (const project of projects) {
      const figure = document.createElement("figure");
      figure.className = "gallery-item";

      const image = document.createElement("img");
      image.src = project.src;
      image.alt = project.alt;
      image.loading = "lazy";

      const caption = document.createElement("figcaption");
      caption.textContent = project.title;

      figure.append(image, caption);
      gallery.append(figure);
    }
  } catch {
    emptyState.textContent = "Project photos are temporarily unavailable.";
  }
}

loadProjects();