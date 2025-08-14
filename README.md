
# 7dt-slides: Teaching Site with Slidev & Vue

This project is a [Slidev](https://github.com/slidevjs/slidev)-powered site for teaching topics like Micro:bit, Python, and Cybersecurity. Content is authored in Markdown and enhanced with Vue components and custom layouts.

## Quick Start

1. Install dependencies:
	- `pnpm install` (or `nci` if using [@antfu/ni](https://github.com/antfu/ni))
2. Start the dev server:
	- `pnpm dev` (or `nr dev`)
3. Open <http://localhost:3030> in your browser.

## Project Structure

- `slides.md`: Main slide deck
- `pages/`: Lesson Content (Markdown)
- `components/`, `layouts/`: Vue components and custom layouts
- `public/img/`: Images and static assets
- `snippets/`: Reusable code samples (Python, TypeScript)
- `.github/workflows/deploy.yml`: GitHub Pages deployment workflow

## Authoring Slides & Lessons

- Use frontmatter (`---`) for slide metadata (title, layout, background, etc.)
- Embed Vue components directly in Markdown
- Reference images from `public/img/`
- Use Mermaid diagrams and code blocks for examples
- Add a new slide in pages

## Build & Deployment

- Build: `pnpm build` (or `nr build`)
- Output: `dist/` folder
- Deploy: Automated via GitHub Actions to GitHub Pages

## Conventions

- Prefer `pnpm` for package management, but `nci`/`nr` are supported
- Keep lessons modular (one topic per Markdown file)
- Use Slidev/Markdown/Vue idioms for authoring

## External Integrations

- **Slidev**: Main framework
- **Vue**: Custom components/layouts
- **Mermaid**: Diagrams in Markdown
- **GitHub Pages**: Static site hosting
- **Netlify/Vercel**: Config files present, but main deploy is via GitHub Pages

---

For more details, see `.github/copilot-instructions.md` and `.github/workflows/deploy.yml`.
