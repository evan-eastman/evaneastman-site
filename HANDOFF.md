# Handoff — evaneastman-site

Last updated: 2026-07-19 (favicon added; Wertheim college/building name
fixes on the front page).

## Status

**Site**: live at https://evaneastman.com with valid HTTPS. CNAME file
committed on `main`; Quarto copies it into `_site/` on each render so
it lands in the `gh-pages` branch on publish. GitHub Pages auto-detects
the domain and re-issues the Let's Encrypt cert as needed (current cert
covers both apex and `www.evaneastman.com`, expires 2026-08-23,
GitHub auto-renews ~30 days before).

**Analytics**: Cloudflare Web Analytics wired in via `_quarto.yml`
`include-in-header`. Token is bound to `evaneastman.com` in the
Cloudflare dashboard (Analytics & Logs → Web Analytics). Privacy-
respecting (no cookies, no consent banner needed); reports country,
referrers, top pages, browsers, and OS. Data appears in the dashboard
within a few minutes of each visit.

**Home PC**: working copy at `C:\Users\Evan\Projects\evaneastman-site\`,
all work pushed to `origin/main` and `origin/gh-pages`. Working tree
clean as of session close.

**School/work PC**: still on Dropbox — follow "Setting up the other
machine" below the next time you sit there. This session didn't touch
the Dropbox copy.

**Content**: seven navbar pages — `index` (About), `research`,
`teaching`, `presentations`, `service`, `awards`, `cv`. SSRN links
across working/published papers; bio finalized; custom domain shipped.

The old `other.qmd` was split (2026-07-15) into three dedicated pages:
`presentations.qmd` (Conferences, Invited Talks academic/professional,
full Conference Presentations, Discussant Talks, Panels — transcribed
from the CV), `service.qmd` (comprehensive: editorial, reviewing,
associations, FSU service, doctoral committees, memberships), and
`awards.qmd` (full Awards & Honors). Service/editorial and talks now
live ONLY on these pages — don't re-add them to Research.

`research.qmd` now has a **Papers Under Review** section (between
Publications and Working Papers) in addition to Working Papers.

The front page (`index.qmd`) has an FSU-gold **symposium announcement
box** that a small inline `<script>` relocates into the About left
column, under the link buttons (`.about-entity`). It's currently
generic ("Information on the 2027 meeting is coming soon"); update the
`symposium-box__body` text when the 5th-symposium CFP/deadline is
final (Jan 21–23, 2027, Tampa Hilton Downtown; official page
`wertheim.fsu.edu/rmiresearchsymposium`). Box styling lives in
`styles.scss` (`.symposium-box`, `$gold: #CEB888`).

## What's left to add (next session ideas)

- Update the front-page **symposium box** once the 5th-symposium CFP /
  submission deadline is finalized — edit `symposium-box__body` in
  `index.qmd` (currently "Information on the 2027 meeting is coming
  soon"). Official page lists Jan 21–23, 2027 (Tampa) and a Sept 1
  deadline, but Evan indicated the due date isn't locked yet.
- More SSRN links — several published papers (#3, 4, 5, 6, 8, 9, 10, 11
  from this session's prompt) weren't added because no IDs were
  available at the time. Working papers without links are #2, 5–13 in
  the same list. Easiest workflow: copy IDs off your SSRN author page.
- Photo polish: current is 800×1000 / 92 KB. Replace if you want a
  different shot.
- Optional: `[Slides]` iconify link on working papers with public
  slide decks.
- Visual QA on phone / different browsers if you haven't already.

## Standard workflow (re-publish)

Now that the initial setup is behind us, every future change is just:

```powershell
cd "$env:USERPROFILE\Projects\evaneastman-site"
git pull
# ... edit, quarto preview to QA ...
git add .; git commit -m "..."
git push origin main
quarto publish gh-pages --no-prompt --no-browser
```

`quarto publish gh-pages` re-renders, pushes to `gh-pages`, and GitHub
Pages serves the update within a minute or two. CNAME is preserved on
every publish because it lives in the source tree at repo root.

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
2. Authenticate: `gh auth login` (web browser flow).
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
- **Quarto preview watcher misses some external file writes.** When
  files are edited via tooling that doesn't trip the inotify watcher
  (Claude's Edit tool is one example), preview's auto-rebuild can run
  on stale input — the rendered HTML stays unchanged even though
  `_site/research.html` shows a fresh mtime. Fix: stop preview, run a
  full `quarto render`, restart preview. Browser-edit-and-save in the
  IDE does *not* hit this.
- **First publish to GitHub Pages is a one-time gotcha.** `quarto
  publish gh-pages --no-prompt` fails on a fresh repo with "the remote
  origin does not have a branch named 'gh-pages'". The branch has to
  pre-exist on origin. This session fixed it by `git push origin
  main:gh-pages` to seed it; Quarto's first publish then replaced the
  content. No longer relevant — `gh-pages` exists on origin, so
  re-publishes via `--no-prompt` work fine.
- **Cloudflare DNS records must be "DNS only" (gray cloud)**, not
  "Proxied" (orange cloud), for GitHub Pages' cert provisioning to
  succeed. Apex `evaneastman.com` is four A records to
  `185.199.108.153 / .109.153 / .110.153 / .111.153`;
  `www.evaneastman.com` is a CNAME to `evan-eastman.github.io`. All
  gray-cloud.
- **Apex domains can't use CNAME records** (RFC restriction). Use A
  records for the bare domain. CNAMEs are fine for subdomains like
  `www`.
- **Iconify identifiers must use the canonical set prefix.** `ai` (an
  older alias for academicons) returns 404 from the Iconify CDN. Use
  `academicons:ssrn`, `academicons:doi`, etc. Other sets in use:
  `simple-icons:googlescholar` for the Scholar icon.
- **Auto-mode classifier blocks `git push origin main` without
  pre-authorization.** Default classifier behavior treats pushes to the
  default branch as PR-bypass. The `autoMode.allow` rules in
  `.claude/settings.local.json` document why this project is an
  exception (single-author static site). Self-modification of
  `.claude/settings.local.json` itself is also blocked — the file has
  to be authored by you (paste via the `!`-prefixed PowerShell
  here-string in this session's history, or edit by hand), not by
  Claude on your behalf.
- **`.claude/settings.local.json` is gitignored and machine-local.**
  The publish-workflow permission rules don't sync across machines.
  When you bring up the school PC, recreate the same file there using
  the same JSON — see the 2026-05-26 history entry below for content.

## Recent history

- 2026-07-19 — Added a **favicon** (`files/favicon.svg`, wired via
  `favicon:` in `_quarto.yml`): garnet `#782F40` rounded square with an
  "EE" monogram in FSU gold `#CEB888`. The letterforms are eight plain
  `<rect>` elements, NOT SVG `<text>` — font-based favicons resolve to
  whatever the OS provides and go blurry at 16px; rectangles stay crisp
  and deterministic. Gold-on-garnet is 4.8:1 contrast (clears WCAG AA,
  but roughly half of white-on-garnet's 9.2:1) — if it ever reads too
  soft in the tab strip, change the `<g fill>` to `#ffffff`, or split
  the difference with `#E0D0A8` (~6.5:1). SVG favicons cover Chrome,
  Edge, Firefox, and Safari 17+; no `.png`/`.ico` fallback is in place,
  so legacy-Safari bookmark bars won't show it. **Chrome caches
  favicons hard** — Ctrl+Shift+R if the old default icon persists.
  Also fixed two errors in the `index.qmd` contact block: "Wertheim
  Center for Business Excellence" → **Herbert** Wertheim Center for
  Business Excellence, and "Herbert Wertheim College **for** Business"
  → College **of** Business. The bio paragraph was already correct.
  Deliberately left `service.qmd` committee names alone — the 2026 item
  says "Wertheim College" while 2020–2025 items say "College of
  Business", which is historically accurate given the college's
  renaming.
- 2026-07-15 — Big content session. (1) Added a **Papers Under Review**
  section to `research.qmd`, moving six papers up from Working Papers.
  (2) Front page: added an **FSU Profile** button (`person-badge` icon,
  `business.fsu.edu/person/evan-eastman`), an **Education** section
  (Ph.D. UGA 2017, B.S. Penn State 2012), and the **symposium
  announcement box** (see Content above). (3) Split `other.qmd` into
  **Presentations / Service / Awards** pages, transcribed from the CV;
  navbar is now About · Research · Teaching · Presentations · Service ·
  Awards · CV. (4) Synced the **July 2026 CV**: 2026 Les B. Strickler
  Innovation in Instruction Award; new 2026 conference talks (Oct FMA
  Tampa, Oct NAIC/CIPR Kansas City, Sep UEA Chicago) + a second paper
  on the Aug 2026 ARIA meeting; new Aug 2026 ARIA discussant talk; new
  "Insurer Investments" paper under review; Jingshu Luo added as
  coauthor on the AFS "Capital Market Consequences" paper. Committed
  (`be25f12`), pushed, and published. **Symposium URL note**:
  `business.fsu.edu/rmiresearchsymposium` 301-redirects to
  `wertheim.fsu.edu/rmiresearchsymposium` — site now uses the canonical
  wertheim URL.
- 2026-06-05 — New **Other** navbar page (`other.qmd`) added after CV.
  Migrated *Selected Invited Talks* and *Service & Editorial* out of
  `research.qmd` into it; added a *Conferences* section linking the
  [FSU RMI Research Symposium](https://business.fsu.edu/rmiresearchsymposium).
  Linked RMIR (Wiley, `onlinelibrary.wiley.com/journal/15406296`) and
  SRIA (`southernrisk.org`) inline within Service & Editorial rather
  than as separate highlight sections — avoids duplication, and these
  items now live ONLY on the Other page. Also added `[Published]`
  links to three papers: JIR *Accounting Standards and Gains Trading*
  (NAIC, `content.naic.org/research/jir/accounting-standards-and-gains-trading`)
  and the two forthcoming NAAJ papers — *Healthy Competition?*
  (Frederick/Yang, doi 10.1080/10920277.2026.2664596) and *Actuarial
  Implications of Changes in Financial Reporting* (Yang/Carson, doi
  10.1080/10920277.2026.2639547). **Caution learned**: the two NAAJ
  DOIs are easy to swap — `2639547` is the Carson/Yang paper (titled
  "Actuarial Implications…"), NOT a companion piece to Healthy
  Competition. Verified author/title via the Crossref API
  (`api.crossref.org/works/<doi>`) since tandfonline 403s automated
  fetches.
- 2026-05-26 — Cloudflare Web Analytics wired in. Beacon snippet added
  to `_quarto.yml` `include-in-header` so it loads on every rendered
  page. Privacy-respecting (no cookies, no consent banner), country-
  level geo, referrers, top pages, browsers/OS. Token configured at
  Cloudflare dashboard, bound to `evaneastman.com`. Also created
  `.claude/settings.local.json` (gitignored) with `permissions.allow`
  and `autoMode.allow` entries for `git push origin main` and
  `quarto publish gh-pages --no-prompt --no-browser` so future
  sessions can run the publish workflow without the auto-mode
  classifier blocking. **Note**: the classifier blocks self-
  modification of that settings file, so Evan wrote it himself via a
  `!`-prefixed PowerShell here-string. Reproduce on the school PC by
  pasting the same JSON. `.gitignore` extended to exclude
  `.claude/settings.local.json`.
- 2026-05-25 — Custom domain shipped. Added `CNAME` at repo root (Quarto
  auto-copies into `_site/`); pushed; re-published. GitHub auto-detected
  the domain, issued a Let's Encrypt cert covering both apex and `www`,
  expires 2026-08-23. Enabled HTTPS enforcement via
  `gh api -X PUT repos/evan-eastman/evaneastman-site/pages -F https_enforced=true`.
  Site verified live at https://evaneastman.com.
- 2026-05-25 — DNS configured at Cloudflare. Four A records at apex →
  GitHub IPs (185.199.108-111.153); CNAME for `www` →
  `evan-eastman.github.io`. All "DNS only" (gray cloud). Propagation
  verified via whatsmydns.net before publish.
- 2026-05-25 — First publish to GitHub Pages succeeded after seeding
  `gh-pages` branch on origin via `git push origin main:gh-pages`.
  Quarto's first publish then rewrote contents to the rendered site.
  Live initially at `https://evan-eastman.github.io/evaneastman-site/`
  before the custom domain was wired in.
- 2026-05-25 — Added SSRN links across the bibliography. Working papers:
  *A Text-Based Measure* (Miller/Wang, 5624330), *Climate Risk and
  Commercial Property* (Buschbom/Wang/Zhou, 5841862). Published papers
  (added alongside existing `[Published]`): *Risk Mgmt & Corporate
  Lifecycles* (JCF, 4608575), *ERM & Corporate Tax Planning* (JRI,
  3717865), *Accounting-Based Regulation* (TAR, 3282300). Convention:
  `[SSRN]` first, then `[Published]` (chronological — working paper
  precedes journal version).
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
