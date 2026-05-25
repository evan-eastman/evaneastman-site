# Handoff — evaneastman-site

Last updated: 2026-05-24 (end of second session).

## Status

**Home PC**: migrated. Project lives at
`C:\Users\Evan\Projects\evaneastman-site\`, builds cleanly with
`quarto render`, syncs via `github.com/evan-eastman/evaneastman-site`
(public). The Dropbox copy at `C:\Users\Evan\Dropbox\Website\` has been
deleted (recoverable from Dropbox web UI for 30 days if needed).

**School/work PC**: still on Dropbox — follow "Setting up the other
machine" below the next time you sit there.

**Content**: all four pages (`index`, `research`, `teaching`, `cv`) are
populated with real content. Bio is finalized; URLs filled in; icons
rendering. Site has not been visually QA'd on all browsers yet, but
renders correctly under `quarto preview`.

**Publishing**: still not pushed to a host. DNS for `evaneastman.com`
still needs to be pointed.

**Uncommitted work**: this session's changes (research/teaching content,
font swap, iconify fix, bio rewrite, URL fills) have not been committed
yet. Run `git status` to see; recommend committing in 1–2 logical
commits before publishing.

## Next session — pick up here

In rough priority order:

1. **Commit current state.** `git status` will show ~5 modified files
   (`research.qmd`, `teaching.qmd`, `index.qmd`, `_quarto.yml`,
   `styles.scss`, `HANDOFF.md`). Recommend one commit for content
   (`research`/`teaching`/`index`) and a second for theming
   (`styles.scss`/`_quarto.yml`).
2. **Visual QA.** Click through the site under `quarto preview` and
   tell Claude what to tweak (spacing, icon size, layout).
3. **Publish to GitHub Pages.** `quarto publish gh-pages` from the
   project root. Site lands at
   `https://evan-eastman.github.io/evaneastman-site/`. (Quarto will
   create the `gh-pages` branch and push automatically.)
4. **Point DNS.** In your registrar, add a CNAME record for
   `evaneastman.com` → `evan-eastman.github.io`. Then add a `CNAME`
   file in the repo root containing `evaneastman.com`, commit, push,
   re-publish. README "Publishing" section has more.
5. **Optional polish:** review the bio prose with a fresh eye;
   double-check coauthor names and middle initials in `research.qmd`;
   add a `[Slides]` link to any working papers with public slide decks.

## Working across machines

The repo is the source of truth. On each machine:

```powershell
cd "$env:USERPROFILE\Projects\evaneastman-site"
git pull          # before starting work
# ... edit, quarto preview, etc. ...
git add .; git commit -m "..."
git push          # before walking away
```

If a `git pull` produces conflicts because you forgot to push from the
other machine, edit the marker blocks (`<<<<<<<` / `=======` /
`>>>>>>>`) by hand, then `git add` and `git commit`.

## Setting up the other machine

On the work/school PC where the project still lives in Dropbox:

1. Install the GitHub CLI: `winget install --id GitHub.cli`.
2. Authenticate: `gh auth login` (web browser flow, like you just did).
3. Clone into Projects: `git clone https://github.com/evan-eastman/evaneastman-site.git "$env:USERPROFILE\Projects\evaneastman-site"`.
4. Confirm the new copy renders: `cd` in, run `quarto render`.
5. Delete the Dropbox copy at `C:\Users\Evan\Dropbox\Website\evaneastman-site\` (the junction in `.quarto/` there needs `cmd /c rmdir` to remove, not `Remove-Item -Recurse`, or it will delete the cache target).
6. The non-Dropbox build cache at `C:\Users\Evan\quarto-build\evaneastman-site\` on that machine is now orphaned — safe to delete.

## Known quirks

- **Never put this project back inside Dropbox.** `quarto render` will
  fail on cleanup with `os error 32`. See the bottom of README.md for
  the full story.
- **`gh` may not be on PATH in old terminals.** If you installed `gh`
  in a previous session, terminals open from before that install won't
  see it. Close and reopen the terminal (or Claude Code session) and
  `gh` will resolve normally.
- **`HANDOFF.md` is tracked in git** so it syncs across machines, but
  `_quarto.yml` has `render: ["*.qmd"]` which keeps it out of the
  rendered `_site/`. Don't remove that line unless you also want this
  file to appear as a page on the public site.
- **GitHub repo is public.** Anything you commit (including this file)
  is visible at `github.com/evan-eastman/evaneastman-site`. Keep
  anything sensitive out of the repo, or switch the repo to private in
  GitHub settings.
- **`quarto render` kills `quarto preview`.** If preview is running and
  Claude (or anyone) runs `quarto render`, the preview server crashes
  with exit code 1. Workflow: let preview do the rebuilding when files
  change; only run an explicit `quarto render` when preview is stopped.
  Exception: a *full* `quarto render` (no file argument) is sometimes
  needed to re-inject the iconify `<script>` tag — a single-file
  `quarto render research.qmd` won't add the dependency. If preview
  dies after that, just restart it.
- **Iconify identifiers must use the canonical set prefix.** `ai` (an
  older alias for academicons) returns 404 from the Iconify CDN. Use
  `academicons:ssrn`, `academicons:doi`, etc. Other sets in use:
  `simple-icons:googlescholar` for the Scholar icon.

## Recent history

- 2026-05-24 — Bio paragraphs rewritten by Evan in `index.qmd`: title is now "Independent Life and Accident Insurance Associate Professor and Research Coordinator for the Risk Management and Insurance Center"; research focus reframed as "empirical archival insurance economics" with active areas in financial accounting, taxation, corporate risk management, and real estate. Contact block expanded with full mailing address.
- 2026-05-24 — Iconify prefix bug fixed: `ai:ssrn` and `ai:doi` returned 404 from the Iconify CDN (the `ai` prefix appears deprecated). Replaced site-wide with `academicons:ssrn` and `academicons:doi`. **Lesson**: always test an iconify identifier with `https://api.iconify.design/<set>:<icon>.svg` before relying on it in a Quarto shortcode — the Lua filter renders the tag whether or not the icon resolves.
- 2026-05-24 — `research.qmd` per-entry links now render with iconify icons (extension vendored at `_extensions/mcanouil/iconify/`): `academicons:ssrn` for `[SSRN]` links, `academicons:doi` for `[Published]` links. Pattern: `[[{{< iconify academicons ssrn >}} SSRN](url)]`. Outer brackets preserved for a tag/button look.
- 2026-05-24 — FSU RMI Center URL filled in across both spots in `index.qmd` (sidebar `links:` entry and inline bio): `https://insurancecenter.business.fsu.edu/`.
- 2026-05-24 — `teaching.qmd` populated: 5 FSU courses (RMI 3011 / 4115 / 4292 / 5710 / 6395) + 1 UGA course (RMIN 4000), each linking to FSU's mobile catalog (`m.fsu.edu/default/course_catalog/detail?area=RMI&course=RMI+XXXX&term=all`). Doctoral Mentoring section lists 3 FSU committee members (Carrillo, Cather, Telljohann — all 2025 grads) and 2 external (Qi at UNT, Yang at UGA). Note: FSU bulletin lists RMI 4115 as "Lifecycle Risk Management"; CV (and this page) uses "Life/Health Insurance" — verify with Evan if this matters.
- 2026-05-24 — Site font switched to Open Sans (FSU brand): Google Fonts loaded via `_quarto.yml` `include-in-header`; `styles.scss` `$font-family-sans-serif` updated to lead with `"Open Sans"`. Prior config declared `"Inter"` but never loaded it, so the page silently fell back to system Segoe UI.
- 2026-05-24 — `research.qmd` restructured to mirror legacy site's three-bucket convention: `## Publications` (14 refereed: 3 forthcoming + 11 published), `## Working Papers` (19, merging former Under Review + Working Papers into one flat list, no status labels), `## Other` (with `### Selected Invited Talks` and `### Service & Editorial` as sub-sections). DOIs/SSRN links cover ~80% of entries. Hard breaks within `.pub-entry` blocks use explicit `<br>` tags (PowerShell 5.1 Get-Content/Out-File mangled UTF-8 in an earlier attempt at trailing-two-space breaks).
- 2026-05-23 — Iconify extension switched from unmaintained
  `quarto-ext/iconify` to actively-maintained `mcanouil/quarto-iconify`
  v3.2.1, vendored at `_extensions/mcanouil/iconify/`.
- 2026-05-23 — Photo resized from 3302×4127 / 2.5 MB to 800×1000 / 92 KB
  JPEG q85. Original preserved at `files/profile-original.jpg`.
- 2026-05-23 — `_quarto.yml` footer email bracket bug fixed; LinkedIn
  and GitHub footer entries removed. `index.qmd` photo path, email,
  Google Scholar, and SSRN URLs corrected.
- 2026-05-24 — Migrated from `Dropbox/Website/evaneastman-site/` to
  `Projects/evaneastman-site/`; initialized git, created public GitHub
  repo, verified `quarto render` succeeds. README rewritten for new
  workflow. `_quarto.yml` updated to render only `.qmd` files.

Full history beyond this is in `git log`.
