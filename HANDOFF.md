# Handoff — evaneastman-site

Last updated: 2026-08-14 (Risk Theory Society page built from Evan's
tracking workbook and left unlisted, pending his call on publishing;
earlier the same day: new CV export and the five site edits that
followed from diffing it, 2027 symposium call for papers published,
Insurance Tycoon simulation linked from Teaching).

## Status

**Site**: live at https://evaneastman.com with valid HTTPS. CNAME file
committed on `main`; Quarto copies it into `_site/` on each render so
it lands in the `gh-pages` branch on publish. GitHub Pages auto-detects
the domain and re-issues the Let's Encrypt cert as needed (current cert
covers both apex and `www.evaneastman.com`, expires 2026-10-22,
GitHub auto-renews ~30 days before — the 2026-08-23 cert renewed on
schedule without intervention).

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

There are two **unlisted** pages, `family-tree.qmd` (the ARIA academic
family tree) and `rts.qmd` (the Risk Theory Society publication
record). Neither is in the navbar and nothing on the site links to
them, so they are reachable only by direct URL. Each carries
`<meta name="robots" content="noindex, nofollow">` and `search: false`,
and a post-render hook keeps them out of `sitemap.xml` (see Known
quirks). Unlisted is not private — the repo is public and the page is
served to anyone with the URL.

`rts.qmd` is built from a spreadsheet Evan maintains,
`files/RTSPublicationTracking_2025.xlsx`: 292 papers across 31 meetings
(1984, then 1994–2024) and 37 meetings (1991–2027). The page carries
headline figures, three SVG charts (papers and publication outcome by
year, top journals, membership and attendance), a searchable table of
every paper, and the meeting history. `tools/build-rts-data.py` reads
the workbook and rewrites the block between
`<!-- BEGIN GENERATED DATA -->` and `<!-- END GENERATED DATA -->` in
`rts.qmd`; the page computes every displayed number from that blob at
load time, so nothing on it can drift from the workbook. Refresh with
`py -3 tools/build-rts-data.py`, then render.

Two rules for that page. **The workbook is gitignored on purpose** —
committing it to a public repo publishes the raw data, which is the
thing the unlisted page is trying to stage. Keep it on disk and in
Dropbox. And **a blank journal means "not recorded," never
"unpublished"** — 105 of the 292 papers have no publication recorded,
and the page says so in three places because it is making public
statements about named scholars' work. Don't relabel those cells.

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
column, under the link buttons (`.about-entity`). As of 2026-08-14 it
carries the live 5th-symposium call for papers: Jan 21–23, 2027 at the
Tampa Hilton Downtown, submissions due **September 15, 2026**, links to
the CFP PDF (`files/rmi-research-symposium-2027-cfp.pdf`) and the
official page, and the submission address. **After September 15, 2026**
switch the box from call-for-papers to program details — a comment in
`index.qmd` marks the spot. Box styling lives in `styles.scss`
(`.symposium-box`, `$gold: #CEB888`); `.feature-entry` is its
full-width sibling for callouts in the main content column.

`teaching.qmd` opens with a **Teaching Innovation** section linking
**Insurance Tycoon**, Evan's homeowners underwriting simulation, at
`https://insurance-tycoon-production.up.railway.app/`. That is a
Railway deployment URL — if the app moves to a custom domain, the link
needs updating. The simulation is Evan's own work and deliberately
carries **no** award mention: the 2026 Les B. Strickler Innovation in
Instruction Award was shared with Cassandra R. Cole and Kyeonghee Kim
for a joint ARIA session in which each presenter showed their own work.
Keep the award on `awards.qmd` and the simulation on `teaching.qmd`;
don't re-link them.

## What's left to add (next session ideas)

- **RTS page — decide whether it goes public.** Built 2026-08-14 as an
  unlisted page so Evan can send the URL to RTS leadership first. If
  they are comfortable, add a navbar entry in `_quarto.yml` and drop
  the `robots` meta and `search: false` from `rts.qmd`.
- **RTS data gaps** worth filling in the workbook, in rough order of
  value: the 2025 papers (the meeting is recorded with 10 papers but no
  program), 1985–1993 (no papers recorded at all), and the 105 papers
  with no publication outcome recorded. The 2021 `date` cell parsed as
  a real date rather than text, so the build script drops it — retype
  it as text (e.g. `April 9-11`) and it will appear.
- Swap the front-page **symposium box** from call-for-papers to program
  details after the **September 15, 2026** submission deadline passes.
- The August 2026 ARIA **Strickler award demonstration** is on neither
  the CV nor the site. Worth adding to the CV on the next pass — Evan's
  call.
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

- **A GitHub Pages build can hang, leaving the live site stale after a
  successful publish.** Happened 2026-08-06: `quarto publish` pushed the
  rendered site to `gh-pages` (`501623b`) and returned success, but the
  Pages builder stuck in `building` for ~20 hours with `duration: 0` and
  no error, so evaneastman.com kept serving the previous build. Publish
  success does not confirm the site went live. Check the build state:

  ```powershell
  gh api repos/evan-eastman/evaneastman-site/pages/builds/latest --jq '.status, .commit, .duration'
  ```

  A healthy build reports `built` in about 20 seconds. If it reads
  `building` with `duration: 0` and an `updated_at` equal to
  `created_at`, it is hung. Request a fresh build:

  ```powershell
  gh api -X POST repos/evan-eastman/evaneastman-site/pages/builds
  ```

  Verify the live page with `curl`, not a browser — browser and
  WebFetch caches both mask the result.
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
- **Every render runs a Python post-render hook.** `_quarto.yml` has
  `post-render: py -3 tools/unlist-noindex-from-sitemap.py`, which
  drops noindex pages from `_site/sitemap.xml`. Quarto writes every
  rendered page into the sitemap whenever `site-url` is set and offers
  no per-page opt-out, so without this the sitemap advertises the URL
  of a page whose own meta tag asks crawlers to ignore it. The script
  keys off the rendered HTML's `robots` meta tag, not a filename —
  marking a future page noindex needs no change to it. **Any machine
  that renders this site needs Python on PATH via the `py` launcher**
  (a stock python.org install provides it). Without it `quarto render`
  fails at the post-render step. The script itself no-ops harmlessly if
  `sitemap.xml` is missing, and takes an optional path argument so you
  can run it against a fixture instead of a real build.
- **`.claude/settings.local.json` is gitignored and machine-local.**
  The publish-workflow permission rules don't sync across machines.
  When you bring up the school PC, recreate the same file there using
  the same JSON — see the 2026-05-26 history entry below for content.
- **Quarto copies only the files in `files/` that a page actually
  links to.** Verified 2026-08-14: `_site/files/` holds four files, not
  six — `profile-original.jpg` and the RTS workbook are both in
  `files/` and neither is copied, because nothing references them. So
  an unreferenced file in `files/` does not reach the published site.
  Don't lean on that alone for anything sensitive: add a link and it
  ships on the next render, which is why the RTS workbook is
  gitignored as well.
- **`rts.qmd` holds ~83 KB of generated JSON.** Don't hand-edit the
  block between the `BEGIN/END GENERATED DATA` markers — edit the
  workbook and re-run `py -3 tools/build-rts-data.py`, which rewrites
  the block in place. The script prints coverage counts and warns about
  malformed cells; read that output, it is how the 2021 date coercion
  and the empty-marker convention (`.`, not blank) surfaced.

## Recent history

- 2026-08-14 — **Risk Theory Society page** (`rts.qmd`) built from
  Evan's tracking workbook, unlisted like `family-tree.qmd`. Four
  headline figures, three hand-rolled SVG charts, a searchable table of
  all 292 papers, and the 37-meeting history.
  `tools/build-rts-data.py` extracts the workbook into the page. No R
  engine, no CDN charting library, no separate data file — the page is
  self-contained, so there is no public JSON endpoint sitting next to
  an unlisted page. The workbook is gitignored. Not yet published;
  waiting on Evan's call about whether RTS should see it first.
- 2026-08-14 — **Insurance Tycoon** linked from a new Teaching
  Innovation section at the top of `teaching.qmd`, in a gold
  `.feature-entry` box (new in `styles.scss`, the full-width sibling of
  `.symposium-box`). First pass also put the sim on `awards.qmd` and
  `presentations.qmd` and framed it as the thing that won the Strickler
  award; that was wrong and got reverted. **Lesson**: an award and a
  linked artifact are separate facts — the Strickler was shared with
  Cassandra R. Cole and Kyeonghee Kim for a session in which each
  presenter showed their own work, so binding the two implied both
  joint authorship of the simulation and a narrower award than the one
  actually given. Ask who owns what before co-locating them.
- 2026-08-14 — **2027 RMI Symposium call for papers** published. The
  front-page box moved from placeholder to the live call, and the
  `presentations.qmd` Conferences section expanded from a one-line
  pointer to the full CFP (deadline, October 15 notification, PDF-to-
  email submission with subject line, invitation-only note). The CFP
  PDF was renamed on the way in — Evan dropped
  `call_for_papers_RMIResearchSymposium2027_v08_10_26.pdf` into
  `files/` and it now serves as `rmi-research-symposium-2027-cfp.pdf`,
  keeping the internal version stamp out of the public URL. Convention:
  rename anything with a version suffix before it gets a public link.
- 2026-08-14 — **New CV export**, and five site edits that came from
  diffing all 19 pages against the site rather than from anything
  mentioned in conversation: `index` job title → **Director of
  Research**, RMI Center; "Climate Risk and the Cost of Commercial
  Property Insurance" → Papers Under Review under its current title;
  **Adam Al-Rubaee** added as dissertation chair (`service`,
  `teaching`); **GEB 6931** and **RMI 6980** added to `teaching` with
  no catalog links (GEB 6931 is a special-topics shell number whose
  catalog title doesn't match, and the FSU catalog is JS-rendered so
  links can't be verified with `curl`); stale `(scheduled)` tags
  dropped from Aug 2026 ARIA and both May 2026 meetings. Left off the
  site by Evan's choice: the *Contemporary Accounting Research*
  conditional acceptance, and the CV's Works in Progress section.
  **Lesson**: diff the whole CV against every page on each new export.
- 2026-08-06 — **Senior Editor, *Journal of Risk and Insurance*
  (2026–present)** added to `service.qmd` Editorial, above the RMIR
  Associate Editor line. Journal link is
  `onlinelibrary.wiley.com/journal/15396975` — Wiley 403s automated
  fetches, so the ISSN (1539-6975 → *Journal of Risk & Insurance*,
  Wiley) was confirmed via the Crossref API instead, same trick used
  for the NAAJ DOIs in the 2026-06-05 entry. Also moved **Homeowners
  Insurance and Housing Prices** (Kim, Zhou) out of Papers Under Review
  into Working Papers in `research.qmd`, SSRN link intact. **`files/cv.pdf`
  is a static export and still reflects neither change** — re-export it
  when the next batch of CV edits is ready.
- 2026-07-31 — Added the **ARIA Academic Family Tree** as an unlisted
  page (`family-tree.qmd`, ~1,100 lines), live at
  `https://evaneastman.com/family-tree.html`. Interactive d3 tree of
  doctoral advising lineages in insurance and risk management: 288
  people, 81 advisors, 45 universities, 52 root advisors, plus eight
  co-advising edges drawn as dashed lines. Click to expand or collapse,
  hover to trace a lineage back to its root, search by name. The page
  is self-contained by design — the data is an inline
  `window.ARIA_TREE_DATA` JSON blob, the CSS is an inline `<style>`
  block namespaced under `#aria-tree` so it can't collide with the
  site's Bootstrap/cosmo theme, and the only external dependency is
  d3 v7 from the jsDelivr CDN. There is no separate data file and no
  build step: **to correct or add a person, edit the JSON on line 387
  of `family-tree.qmd` directly.** The `stats` object and the
  "Generated" date in the footer are hand-maintained alongside it, so
  update them in the same edit.
  - Unlisted means: no navbar entry, no inbound link from any page,
    `search: false`, and `<meta name="robots" content="noindex,
    nofollow">` via `include-in-header`. It is *not* private.
  - The `#aria-tree *` `box-sizing: border-box` reset at the top of the
    style block is load-bearing. Bootstrap sets that globally, so the
    bug it fixes (the search field's padding pushing it out past 100%
    width and overlapping the toolbar buttons) only appears outside
    Quarto. Don't drop it as redundant — it's what lets the block work
    standalone.
- 2026-07-31 — **Sitemap now excludes noindex pages.** New post-render
  hook `tools/unlist-noindex-from-sitemap.py`, wired via `post-render:`
  in `_quarto.yml`. Quarto puts every rendered page in `sitemap.xml`
  when `site-url` is set, with no per-page opt-out, which defeats the
  point of an unlisted page: the meta tag asks crawlers not to index it
  while the sitemap points them straight at it. Robots honour noindex
  over a sitemap entry, so nothing was actually leaking — but
  advertising the URL is the opposite of what unlisted is for. The
  script parses each `<loc>`, maps it back to the file Quarto wrote,
  and removes the entry if that HTML carries a noindex `robots` meta
  tag. Keying off the page's own declaration rather than a hardcoded
  filename means future unlisted pages need no change here. Verified:
  local and published `sitemap.xml` both carry seven URLs and no
  `family-tree` entry. Adds a Python dependency to `quarto render` —
  see Known quirks.
- 2026-07-31 — **Credited James M. Carson as the tree's originator.**
  Carson assembled the tree from dissertation chairs and presented it
  as the "Six Degrees of Solomon Huebner" in his ARIA presidential
  address, describing it as a work in progress he hoped to post on the
  ARIA website. Citation, now in the page footer: James M. Carson,
  "The ARIA Loop," *Risk Management and Insurance Review*, 2005, Vol.
  8, No. 1, pp. 1–8 — presidential address delivered at the 2004 ARIA
  meeting, Chicago. A bold credit line sits above the tree as well, so
  the page reads as a continuation of his work rather than a
  replacement. Keep both if the page is ever restructured.
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
- 2026-07-19 — **Analytics granularity: evaluated and declined.** Evan
  asked whether visitor tracking could show state/city like his old
  Google Site did. Cloudflare Web Analytics is **country-only with no
  setting to change it**. Confusing point worth remembering: Cloudflare
  *the platform* does expose city/region, but only in the proxy/Workers
  layer — the free WA beacon is a separate, deliberately coarse product.
  Getting city out of Cloudflare would require flipping DNS from
  gray-cloud to **Proxied** plus a Worker reading `cf.city` — rejected,
  because the gray-cloud config is exactly what GitHub Pages needed for
  cert provisioning, and proxying adds SSL-mode/redirect-loop risk to a
  working setup. Alternatives priced out: GA4 (free, city-level, but
  cookies + EU consent-banner obligation the site currently avoids),
  Plausible (~$9/mo, city drill-down, no banner), Umami (free tier).
  **Decision: stay on Cloudflare as-is.** Don't re-open unless the
  requirement changes. Also noted: city-level IP geo is noisy (resolves
  the network, not the person — university traffic often lands on a
  campus NOC or VPN exit), and "which institution is reading me" is NOT
  reliably obtainable from any mainstream tool since GA4 dropped
  Universal Analytics' Network Domain field. Referrers are the better
  signal.
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
