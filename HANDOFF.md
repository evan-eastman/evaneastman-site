# Handoff — evaneastman-site

Last updated: 2026-05-23, mid-session, paused for cross-machine pickup.

## Status: paused pending project-location decision

The site cannot reliably build while it lives inside Dropbox. Pick a
path from the next section, then start a new Claude session on the
other machine and paste in your choice. The build will work
immediately on a non-Dropbox path; no other setup needed beyond
installing Quarto and (optionally) git.

## The Dropbox problem (read once, then forget)

`quarto render` consistently fails inside Dropbox with
"process cannot access the file" (`os error 32`) errors. Confirmed
by experiment on 2026-05-23:

- Two consecutive renders from a non-Dropbox copy of the same source
  files: clean success, all four pages output.
- Same source, same machine, in Dropbox: fails every render at the
  cleanup step.

Root cause: Quarto creates transient `<doc>_files/` directories at
the project root for every rendered document (e.g. `index_files/`),
then deletes them after copying contents to `_site/`. Dropbox's
file watcher grabs OS-level handles on the new directories before
Quarto can delete them. Things we tried and ruled out:

- Setting the `com.dropbox.ignored` NTFS extended attribute on
  `_site/`, `.quarto/`, `site_libs/`. Dropbox still grabs handles
  on freshly-created children inside those directories.
- NTFS junctions redirecting build dirs to a non-Dropbox cache.
  Works for `.quarto/` (it's the one Quarto doesn't realpath-check)
  but Quarto's website renderer refuses to operate on junctioned
  `_site/` or `site_libs/` with "Refusing to remove directory…
  since it is not a subdirectory of the main project directory".
- Stopping Dropbox processes during render. Doesn't help — the
  junction-related Quarto error fires even with Dropbox off.

Bottom line: the project must live outside Dropbox.

## Three options

1. **Move project to `~/Projects/evaneastman-site/`, drop the
   Dropbox copy. Sync between machines via git + GitHub.**
   Gives version history. Plays well with `quarto publish gh-pages`
   if you want to host on GitHub Pages. Recommended.

2. **Move project out of Dropbox, keep the Dropbox copy as a
   passive backup.** Add a `robocopy` one-liner to mirror source
   files into Dropbox after edits. No git required.

3. **Stay in Dropbox.** `quarto preview` (live-reload dev server)
   is more forgiving than `quarto render`, so daily editing mostly
   works; full renders for publishing hit the wall and need
   workarounds each time. Not recommended but possible.

When you start the next session, paste this "Three options" block
and your pick — Claude will proceed from there.

## What's been done this session

- **Iconify extension** — `mcanouil/quarto-iconify` v3.2.1 installed
  at `_extensions/mcanouil/iconify/`. Dropbox-synced, so present on
  whatever machine you sit down at. (The README originally pointed
  at the unmaintained `quarto-ext/iconify`; that's been fixed.)
- **`index.qmd`** — photo path corrected to `files/profile.jpg`;
  email set to `eeastman@wertheim.fsu.edu`; LinkedIn link removed;
  Google Scholar URL set (`user=ksnlHLAAAAAJ&hl=en`); SSRN URL set
  (`per_id=2361505`); body contact email updated.
- **`_quarto.yml`** — footer email fixed (`mailto:[...]` bracket bug
  was breaking the link); LinkedIn and GitHub footer entries
  removed; stale comment on `site-url` removed (domain is now
  registered, so it's no longer aspirational).
- **`files/profile.jpg`** — resized from 3302×4127 / 2.5 MB to
  800×1000 / 92 KB JPEG q85. Original preserved at
  `files/profile-original.jpg` in case you ever need the full-res.
- **README.md** — iconify command corrected; a Dropbox-setup section
  was added but it documents the junction approach we now know is
  incomplete. The README needs a clean rewrite once you pick an
  option above.

None of the above has been visually verified in a browser because
the in-Dropbox render keeps failing — but the source files are
correct and a render from a non-Dropbox copy produced clean output
during the diagnostic.

## What's still to fill in

| Where                            | What                                                                       |
| -------------------------------- | -------------------------------------------------------------------------- |
| `index.qmd` L15, L25             | FSU RMI Center URL (currently `business.fsu.edu/REPLACE` in two places)    |
| `index.qmd` L25–29               | Bio paragraphs — read through; defaults are reasonable but may be off      |
| `research.qmd`                   | Every entry: `[Coauthors]`, `[Paper Title]`, `[Year]`, `[Journal]`, links. Easiest with CV in hand. |
| `teaching.qmd`                   | Two course slots: `RMI XXXX — [Course Title]`, semesters, syllabus PDFs    |
| Domain hosting                   | `evaneastman.com` is registered; needs DNS pointed at whatever host you pick (Quarto Pub, Netlify, or GitHub Pages — decide when ready to publish) |

## Current-machine state (Windows desktop with Dropbox)

If you come back to this box, be aware:

- `.quarto/` at the project root is an NTFS **junction** pointing
  to `C:\Users\Evan\quarto-build\evaneastman-site\.quarto`. Don't
  `Remove-Item -Recurse` it without checking `LinkType` — that
  would delete the cache target, not just the link. Use
  `cmd /c rmdir <path>` (no `/s`) to remove only the link.
- `_site/` and `site_libs/` are real empty directories with
  `com.dropbox.ignored` set.
- The non-Dropbox build cache at
  `C:\Users\Evan\quarto-build\evaneastman-site\` can be deleted at
  any time; Quarto recreates it.

None of this state syncs across machines — junctions and ADS are
filesystem-local. On the other computer the project will just look
like the synced source files: `.qmd`, `_quarto.yml`, `_extensions/`,
`files/`, `styles.scss`, `README.md`, and this `HANDOFF.md`.

## First step on the new machine

1. Install Quarto if not already there: <https://quarto.org/docs/get-started/>.
2. Open this folder in your terminal and read this file.
3. Decide which of the three options above you want.
4. Start a Claude session in the project folder, paste the
   "Three options" section with your pick, and ask to continue.
   The first thing Claude will do is move the project to its new
   home; after that, we're back to filling in placeholders.
