# evaneastman.com — Quarto site

Personal academic website built with [Quarto](https://quarto.org).

## One-time setup

1. **Install Quarto** from <https://quarto.org/docs/get-started/>. Pick the Windows installer.
2. **Drop this folder somewhere stable** — e.g.
   `C:\Users\Evan\Dropbox\Projects\website\` so it's backed up and synced
   across machines.
3. **Add real files**:
   - Replace `profile.jpg` with your headshot (square, ~600×600 works well).
   - Drop your latest CV into `files/cv.pdf`.
   - Update placeholder URLs in `_quarto.yml` and `index.qmd` (email,
     LinkedIn, Scholar, SSRN, FSU RMI page).
4. **(Optional) Install the Iconify extension** for Scholar/SSRN icons:
   ```powershell
   quarto add mcanouil/quarto-iconify
   ```
   (The `quarto-ext/iconify` repo is unmaintained; `mcanouil/quarto-iconify`
   is the actively-maintained fork.)

5. **If the project lives inside Dropbox**, redirect the generated build
   directories to a non-Dropbox location via NTFS junctions. Dropbox's
   file watcher otherwise holds handles on freshly-created files inside
   `.quarto/` and `quarto render` fails with `os error 32` (file in use)
   on cleanup. The `com.dropbox.ignored` attribute alone is not sufficient
   on directories Dropbox is actively watching — junctions are.

   One-time setup, run from the project root:
   ```powershell
   $root  = Get-Location
   $cache = "$env:USERPROFILE\quarto-build\$((Split-Path $root -Leaf))"
   New-Item -ItemType Directory -Path $cache -Force | Out-Null
   foreach ($d in @("_site", ".quarto", "site_libs")) {
     $src = Join-Path $root  $d
     $dst = Join-Path $cache $d
     New-Item -ItemType Directory -Path $dst -Force | Out-Null
     if (Test-Path $src -PathType Container) {
       if (-not (Get-Item $src).LinkType) { Remove-Item $src -Recurse -Force }
     }
     cmd /c mklink /J "`"$src`"" "`"$dst`"" | Out-Null
     Set-Content -Path $src -Stream com.dropbox.ignored -Value 1
   }
   ```
   Source files (`.qmd`, `_quarto.yml`, `styles.scss`, `files/`, `_extensions/`)
   stay in Dropbox and sync across machines. Each machine builds into its
   own local `~/quarto-build/evaneastman-site/` cache. Re-run the snippet
   once per machine.

## Daily workflow

Open a terminal in this folder (PowerShell works fine):

```powershell
quarto preview
```

This launches a live-reloading local server. Edit any `.qmd` file, save,
and the browser tab refreshes automatically. Stop the server with Ctrl+C.

When you're ready to publish a new version, see "Publishing" below.

## File-by-file

| File              | Purpose                                                   |
|-------------------|-----------------------------------------------------------|
| `_quarto.yml`     | Site-wide config: title, navbar, footer, theme, accent.   |
| `index.qmd`       | Landing page. Uses the `trestles` about template.         |
| `research.qmd`    | Publications, working papers, work in progress.           |
| `teaching.qmd`    | Courses and mentoring.                                    |
| `cv.qmd`          | Embeds and links `files/cv.pdf`.                          |
| `styles.scss`     | Custom colors, fonts, and tweaks. Edit to taste.          |
| `files/`          | Static assets the site links to (CV PDF, syllabi, etc.).  |
| `_site/`          | Generated output. Never edit by hand. Add to `.gitignore` if you use git. |

## Adding a new publication

In `research.qmd`, copy an existing `::: {.pub-entry} ... :::` block and
fill in the new entry. That's it. The `.pub-entry` styling in
`styles.scss` handles the spacing and divider lines.

If you'd rather drive this page from your existing `.bib` file later,
Quarto supports that via `bibliography:` and `nocite:` in the page YAML
header — happy to convert when you want.

## Publishing

Two no-git paths, pick one:

### Option A — Quarto Pub (simplest)

```powershell
quarto publish quarto-pub
```

First time, it prompts you to log in. After that, every publish is one
command. Site lives at `evan-eastman.quarto.pub` (or similar) and can be
pointed at your custom domain.

### Option B — Netlify drop

```powershell
quarto render
```

Then drag the generated `_site/` folder onto <https://app.netlify.com/drop>.
Each drop replaces the previous version. Custom domain configured in the
Netlify dashboard.

## Customizing the look

- **Accent color**: change `$primary` in `styles.scss` and `linkcolor`
  in `_quarto.yml`. Both currently set to FSU garnet (#782F40).
- **Theme**: swap `cosmo` in `_quarto.yml` for any
  [Bootswatch theme](https://bootswatch.com/) — `flatly`, `litera`,
  `lumen`, `sandstone`, `journal` are all clean academic options.
- **Fonts**: change `$font-family-sans-serif` in `styles.scss`. A Google
  Fonts import at the top of the file lets you use almost anything.
- **About template**: `trestles` (current) puts the photo to the left of
  the bio. Alternatives are `jolla`, `solana`, `marquee` — see
  <https://quarto.org/docs/websites/website-about.html>.
