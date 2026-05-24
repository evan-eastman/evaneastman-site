# Handoff — evaneastman-site

Last updated: 2026-05-24.

## Status

**Home PC**: migrated. Project lives at
`C:\Users\Evan\Projects\evaneastman-site\`, builds cleanly with
`quarto render`, syncs via `github.com/evan-eastman/evaneastman-site`
(public). The Dropbox copy at `C:\Users\Evan\Dropbox\Website\` has been
deleted (recoverable from Dropbox web UI for 30 days if needed).

**School/work PC**: still on Dropbox — follow "Setting up the other
machine" below the next time you sit there.

**Publishing**: site has not been published yet. DNS for
`evaneastman.com` still needs to point at a host once you pick one (see
README "Publishing" section).

## What's still to fill in

| Where                 | What                                                                       |
| --------------------- | -------------------------------------------------------------------------- |
| `index.qmd` L15, L25  | FSU RMI Center URL (currently `business.fsu.edu/REPLACE` in two places)    |
| `index.qmd` L25–29    | Bio paragraphs — read through; defaults are reasonable but may be off      |
| `research.qmd`        | Every entry: `[Coauthors]`, `[Paper Title]`, `[Year]`, `[Journal]`, links. Easiest with CV in hand. |
| `teaching.qmd`        | Two course slots: `RMI XXXX — [Course Title]`, semesters, syllabus PDFs    |
| Publishing + DNS      | Pick a host (GitHub Pages recommended), run `quarto publish gh-pages`, point `evaneastman.com` DNS at it |

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

## Recent history

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
