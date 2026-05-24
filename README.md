# evaneastman.com — Quarto site

Personal academic website built with [Quarto](https://quarto.org). Source
lives at `github.com/evan-eastman/evaneastman-site`.

## Local setup (per machine)

1. **Install Quarto** from <https://quarto.org/docs/get-started/>.
2. **Install Git** from <https://git-scm.com/download/win> if not already
   installed. The GitHub CLI (`gh`) is optional but makes auth simpler:
   `winget install --id GitHub.cli`.
3. **Clone the repo** somewhere *outside* Dropbox. The build fails inside
   Dropbox due to file-handle conflicts during cleanup — see the bottom of
   this file for the gory detail.

   ```powershell
   git clone https://github.com/evan-eastman/evaneastman-site.git "$env:USERPROFILE\Projects\evaneastman-site"
   cd "$env:USERPROFILE\Projects\evaneastman-site"
   ```

4. **Iconify extension** is already vendored in `_extensions/mcanouil/iconify/`
   and committed to the repo, so it's available immediately after cloning —
   no `quarto add` step needed.

## Daily workflow

```powershell
cd "$env:USERPROFILE\Projects\evaneastman-site"
quarto preview
```

`quarto preview` launches a live-reloading local server. Edit any `.qmd`
file, save, and the browser tab refreshes. Stop with `Ctrl+C`.

When you're done editing:

```powershell
git add .
git commit -m "Describe what changed"
git push
```

## Working from a second machine

```powershell
cd "$env:USERPROFILE\Projects\evaneastman-site"
git pull                       # grab any changes from the other machine
quarto preview                 # edit as usual
git add .; git commit -m "..."
git push
```

If `git pull` reports a conflict (you edited the same file on both
machines), Git will mark the conflicts in the file with `<<<<<<<` / `=======`
/ `>>>>>>>` markers. Edit to resolve, then `git add <file>` and
`git commit`.

## Publishing

Three options, easiest first:

### Option A — GitHub Pages (recommended for this repo)

```powershell
quarto publish gh-pages
```

First run creates a `gh-pages` branch on the GitHub repo, configures
Pages, and pushes the rendered `_site/` there. Subsequent runs just push
updates. Custom domain (`evaneastman.com`) is configured in **Settings →
Pages → Custom domain** on github.com, with a `CNAME` record at the
domain registrar pointing to `evan-eastman.github.io`.

### Option B — Quarto Pub

```powershell
quarto publish quarto-pub
```

First time prompts for a Quarto Pub login. Each publish is one command.
Site lives at `evan-eastman.quarto.pub/<slug>` (or your custom domain).

### Option C — Netlify drop

```powershell
quarto render
```

Then drag `_site/` onto <https://app.netlify.com/drop>. Each drop
replaces the previous version. Custom domain configured in the Netlify
dashboard.

## File-by-file

| File              | Purpose                                                   |
|-------------------|-----------------------------------------------------------|
| `_quarto.yml`     | Site-wide config: title, navbar, footer, theme, accent. The `render: ["*.qmd"]` directive prevents `.md` notes (like `HANDOFF.md`) from being rendered to the public site. |
| `index.qmd`       | Landing page. Uses the `trestles` about template.         |
| `research.qmd`    | Publications, working papers, work in progress.           |
| `teaching.qmd`    | Courses and mentoring.                                    |
| `cv.qmd`          | Embeds and links `files/cv.pdf`.                          |
| `styles.scss`     | Custom colors, fonts, and tweaks. Edit to taste.          |
| `files/`          | Static assets the site links to (CV PDF, headshot, syllabi). |
| `_extensions/`    | Vendored Quarto extensions (currently `mcanouil/iconify`). |
| `_site/`          | Generated output. Gitignored; never edit by hand.         |
| `.quarto/`        | Quarto's local build cache. Gitignored.                   |
| `HANDOFF.md`      | Cross-machine working notes. Tracked in git so it syncs between machines, but excluded from the public site. |

## Adding a new publication

In `research.qmd`, copy an existing `::: {.pub-entry} ... :::` block and
fill in the new entry. The `.pub-entry` styling in `styles.scss` handles
spacing and divider lines.

If you'd rather drive this page from a `.bib` file later, Quarto supports
that via `bibliography:` and `nocite:` in the page YAML header.

## Customizing the look

- **Accent color**: change `$primary` in `styles.scss` and `linkcolor`
  in `_quarto.yml`. Both currently set to FSU garnet (`#782F40`).
- **Theme**: swap `cosmo` in `_quarto.yml` for any
  [Bootswatch theme](https://bootswatch.com/) — `flatly`, `litera`,
  `lumen`, `sandstone`, `journal` are all clean academic options.
- **Fonts**: change `$font-family-sans-serif` in `styles.scss`. A Google
  Fonts import at the top of the file lets you use almost anything.
- **About template**: `trestles` (current) puts the photo to the left of
  the bio. Alternatives are `jolla`, `solana`, `marquee` — see
  <https://quarto.org/docs/websites/website-about.html>.

## Why this project does not live in Dropbox

`quarto render` consistently fails inside Dropbox-synced folders with
`process cannot access the file` (`os error 32`). Root cause: Quarto
creates transient `<doc>_files/` directories at the project root for
every rendered document, then deletes them after copying contents to
`_site/`. Dropbox's file watcher grabs OS-level handles on the new
directories before Quarto can delete them.

We tried the `com.dropbox.ignored` NTFS extended attribute and NTFS
junctions; both have failure modes. The robust fix is to keep the
working copy outside Dropbox entirely. Git + GitHub handles
cross-machine sync.
