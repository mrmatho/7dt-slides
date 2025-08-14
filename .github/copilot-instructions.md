# Copilot Coding Agent Instructions for 7dt-slides

## Project Overview
- This repo is a [Slidev](https://github.com/slidevjs/slidev) presentation site for teaching topics (e.g., Micro:bit, Python, Cybersecurity).
- Slides are authored in markdown (`slides.md`, `pages/*.md`) and enhanced with Vue components (`components/`, `layouts/`).
- Static assets (images, etc.) are in `public/img/`.
- The site is deployed via GitHub Pages using a custom workflow (`.github/workflows/deploy.yml`).

## Developer Workflows
- **Local development:**
  - Use `pnpm install` (or `nci` if using [@antfu/ni](https://github.com/antfu/ni)) to install dependencies.
  - Start dev server with `pnpm dev` (or `nr dev`).
  - Main entry: `slides.md`. Additional lessons in `pages/`.
- **Build & Deploy:**
  - Build with `pnpm build` (or `nr build`).
  - Deployment is automated via GitHub Actions (`deploy.yml`).
  - Output is in `dist/` and published to GitHub Pages.

## Project-Specific Patterns
- **Slidev conventions:**
  - Use frontmatter (`---`) for slide metadata (title, layout, background, etc.).
  - Vue components can be embedded directly in markdown.
  - Custom layouts are in `layouts/` (e.g., `li.vue`).
- **Lesson structure:**
  - Each lesson is a markdown file in `pages/`.
  - Use code blocks for examples (Python, Mermaid diagrams, etc.).
  - Images referenced from `public/img/`.
- **Snippets:**
  - Reusable code samples in `snippets/` (Python, TypeScript).

## External Dependencies & Integrations
- **Slidev**: Main framework for slides.
- **Vue**: Used for custom components/layouts.
- **Mermaid**: For diagrams in markdown.
- **GitHub Pages**: Static site hosting.
- **Netlify/Vercel**: Config files present, but main deploy is via GitHub Pages.

## Examples
- To add a new lesson: create a markdown file in `pages/`, use Slidev frontmatter, and reference images/components as needed.
- To add a custom component: place a `.vue` file in `components/` and import/use in markdown.
- To update deployment: edit `.github/workflows/deploy.yml`.

## Key Files & Directories
- `slides.md`: Master slide deck.
- `pages/`: Lesson content.
- `components/`, `layouts/`: Vue components/layouts.
- `public/img/`: Images for slides.
- `.github/workflows/deploy.yml`: Deployment workflow.
- `snippets/`: Code samples.

## Conventions
- Prefer `pnpm` for package management, but `nci`/`nr` (from @antfu/ni) are supported.
- Use Slidev/Markdown/Vue idioms for slide authoring.
- Keep lessons modular (one topic per markdown file).

---

If unclear, review `README.md` and `.github/workflows/deploy.yml` for current workflows and conventions.
