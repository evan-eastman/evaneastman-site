# Session Progress Log

This file tracks work sessions for continuity. Each entry records what was
done and what to do next.

**Note:** the detailed handoff for this project lives in `HANDOFF.md` at the
repo root (status, known quirks, full recent history). This log is the short
session-by-session record that `/ci` reads at check-in. Keep entries brief and
defer detail to `HANDOFF.md` rather than duplicating it.

---

## Session: 2026-07-19 14:30
**Project:** evaneastman-site (Quarto personal website)
**Objective:** Fix incorrect FSU college/building names on the front page; add
a favicon; confirm whether visitor analytics were in place and where to check.
**Completed:**
- Corrected the `index.qmd` contact block: "Wertheim Center for Business
  Excellence" → **Herbert** Wertheim Center for Business Excellence, and
  "Herbert Wertheim College **for** Business" → College **of** Business. Bio
  paragraph was already correct. Left `service.qmd` committee names alone —
  the 2026 vs 2020–2025 naming split is historically accurate.
- Added `files/favicon.svg` (garnet `#782F40` rounded square, FSU-gold
  `#CEB888` "EE" monogram) and wired it via `favicon:` in `_quarto.yml`.
  Letterforms are plain `<rect>` elements, not SVG `<text>`, so they stay
  crisp at 16px with no font dependency.
- Verified Cloudflare Web Analytics is live: beacon present on all 7 pages
  with a valid token. Dashboard path is Cloudflare → Analytics & Logs → Web
  Analytics → evaneastman.com.
- Evaluated city/region-level tracking and declined it (see Finding).
- Committed (`fefd51d`, `40e7d61`), pushed, published; verified end-to-end
  against the live site.
**Output:** `files/favicon.svg` (new), `_quarto.yml`, `index.qmd`, `HANDOFF.md`
**Finding:** Cloudflare Web Analytics is country-only with no setting to
change it. Cloudflare *the platform* exposes city/region, but only in the
proxy/Workers layer — the free beacon is a separate, coarser product. Getting
city data would require flipping DNS from gray-cloud to Proxied plus a Worker
reading `cf.city`; rejected because gray-cloud is precisely what GitHub Pages
needed for cert provisioning. **Decision: stay on Cloudflare as-is.**
**Next:**
1. Update the front-page symposium box (`symposium-box__body` in `index.qmd`)
   once the 5th-symposium CFP/deadline is final — Jan 21–23, 2027, Tampa
   Hilton Downtown; deadline not yet locked.
2. Backfill SSRN links: published papers #3, 4, 5, 6, 8, 9, 10, 11 and working
   papers #2, 5–13. Easiest via the SSRN author page.
3. Set up the school/work PC — migrate off Dropbox and recreate
   `.claude/settings.local.json` (gitignored, so it does not sync). Recipe in
   `HANDOFF.md` under "Setting up the other machine."
4. Optional: photo polish, `[Slides]` links on working papers, mobile and
   cross-browser visual QA.
**Blocked:** None

---

## Session: 2026-07-31 11:45
**Project:** evaneastman-site (Quarto personal website)
**Objective:** Publish the ARIA academic family tree as an unlisted page on
the site, and keep it out of search indexes.
**Completed:**
- Added `family-tree.qmd`: interactive d3 tree of doctoral advising lineages
  in insurance and risk management (288 people, 81 advisors, 45 universities,
  52 roots, 8 co-advising edges). Self-contained — inline data, inline CSS
  namespaced under `#aria-tree`, d3 v7 from CDN. No navbar entry, no inbound
  links, `search: false`, `robots: noindex, nofollow`. Live at
  `evaneastman.com/family-tree.html`.
- Added `tools/unlist-noindex-from-sitemap.py` and wired it as a Quarto
  `post-render` step. Quarto has no per-page sitemap opt-out, so the sitemap
  was advertising the URL of a page whose meta tag asks crawlers to skip it.
  The script keys off the rendered HTML's robots tag, not a filename.
- Credited James M. Carson as the tree's originator (in-page line plus full
  citation in the footer): "The ARIA Loop," *RMIR* 2005, 8(1), 1–8,
  presidential address, 2004 ARIA meeting.
- Committed (`51b169c`, `99a21bd`, `bc187e6`), pushed, published.
**Output:** `family-tree.qmd` (new), `tools/unlist-noindex-from-sitemap.py`
(new), `_quarto.yml`
**Finding:** Robots honour noindex over a sitemap entry, so nothing was
leaking before the hook — but listing an unlisted page's URL in the sitemap
works against the point of it. Note the site now needs Python on PATH via the
`py` launcher for `quarto render` to complete.
**Next:**
1. Same queue as the 2026-07-19 entry (symposium box, SSRN backfill, school
   PC setup, optional polish) — none of it was touched this session.
2. Family tree: corrections and additions go straight into the inline JSON in
   `family-tree.qmd`; update the `stats` object and the footer "Generated"
   date in the same edit.
**Blocked:** None

---

## Session: 2026-08-06
**Project:** evaneastman-site (Quarto personal website)
**Objective:** Backfill documentation for the 2026-07-31 session, which
shipped and pushed but was never written up; then two content updates.
**Completed:**
- Wrote the 2026-07-31 entry above; added the family tree to `HANDOFF.md`
  Status, three entries to Recent history, and a Known quirks entry for the
  Python post-render dependency.
- `service.qmd`: added **Senior Editor**, *Journal of Risk and Insurance*
  (2026–present) above the RMIR Associate Editor line.
- `research.qmd`: moved **Homeowners Insurance and Housing Prices** (Kim,
  Zhou) from Papers Under Review to Working Papers.
- Rendered, committed, pushed, published.
**Output:** `HANDOFF.md`, `Work/session_progress.md`, `service.qmd`,
`research.qmd`
**Finding:** None.
**Next:**
1. **Re-export `files/cv.pdf`** — Evan has further CV edits coming within a
   day or so and wants them pushed as one batch. The PDF currently reflects
   neither the JRI Senior Editor role nor the paper's move to Working Papers.
2. Otherwise unchanged from the 2026-07-31 entry.
**Blocked:** None


---

## Session: 2026-08-07 11:30
**Project:** evaneastman-site (Quarto personal website)
**Objective:** Find out why yesterday's two content edits were not visible on
the live site, after Evan's PC lost power mid-session.
**Completed:**
- Confirmed nothing was lost to the power failure. `origin/main` was at
  `a3b8df7`, identical to local (0 ahead / 0 behind), and the rendered site
  had reached `origin/gh-pages` as `501623b` at 2026-08-06 12:12 with both
  edits present in the built HTML.
- Diagnosed the real cause: the GitHub Pages build for `501623b` hung. It sat
  in `building` for ~20 hours with `duration: 0`, no error, and `updated_at`
  frozen equal to `created_at`. The live site kept serving `f29bb9a` from
  2026-07-31, which predates both edits.
- Requested a fresh build with
  `gh api -X POST repos/evan-eastman/evaneastman-site/pages/builds`. It
  completed in 21 seconds.
- Verified live with `curl` (browser and WebFetch caches both mask the
  result): `service.html` carries the Senior Editor line, `research.html`
  places Homeowners Insurance and Housing Prices under Working Papers.
- Added a Known-quirks entry to `HANDOFF.md` with the symptom, the
  `gh api .../builds/latest` check, and the rebuild command. Corrected the
  TLS cert expiry there from 2026-08-23 to 2026-10-22 — GitHub renewed it
  automatically, state `approved`, covering apex and `www`.
- Committed and pushed as `ae6c120`.
**Output:** `HANDOFF.md`, `Work/session_progress.md`
**Finding:** `quarto publish` reporting success does not mean the site went
live — it confirms only that the render reached `gh-pages`. The Pages build
is a separate step that can hang silently, and a hung build is invisible from
the repo side. Check `gh api repos/.../pages/builds/latest --jq '.status'`
after any publish; a healthy build reports `built` in about 20 seconds.
**Next:**
1. **Several content updates are coming, including the re-exported
   `files/cv.pdf`.** Evan is stepping away and will return with them. The PDF
   on the site is still the 2026-07-15 export, so it reflects neither the JRI
   Senior Editor role nor the paper's move to Working Papers. Push the batch
   together.
2. After that publish, confirm the Pages build actually completed before
   calling the work done — see the new Known quirks entry in `HANDOFF.md`.
3. Otherwise unchanged from the 2026-07-31 entry: symposium box in
   `index.qmd` (awaiting the final 5th-symposium CFP deadline, Jan 21-23
   2027, Tampa Hilton Downtown); SSRN backfill for published papers
   #3, 4, 5, 6, 8, 9, 10, 11 and working papers #2, 5-13; school PC setup;
   optional photo/`[Slides]`/mobile QA polish.
**Blocked:** None


---

## Session: 2026-08-14 11:09
**Project:** evaneastman-site (Quarto personal website)
**Objective:** Push the new CV export and bring every site page into
agreement with it; then publish the 2027 RMI Symposium call for papers;
then add a link to the Insurance Tycoon teaching simulation.
**Completed:**
- **CV batch (`6ea3a04`).** Read all 19 pages of the new export and
  diffed it against every page. Five site changes followed: `index`
  title is now **Director of Research**, RMI Center (was Research
  Coordinator); "Climate Risk and the Cost of Commercial Property
  Insurance" moved from Working Papers to Papers Under Review under its
  current title; Adam Al-Rubaee added as dissertation **chair** in
  `service` and `teaching`; GEB 6931 and RMI 6980 added to `teaching`;
  stale `(scheduled)` tags dropped from Aug 2026 ARIA and both May 2026
  meetings. Evan chose to leave the CAR conditional acceptance and the
  CV's Works in Progress section off the site.
- **Symposium CFP (`99cda60`).** Front-page box moved from placeholder
  to the real announcement — dates, the September 15 2026 deadline in
  garnet bold, what accepted papers get, links to the CFP PDF and the
  symposium page, and the submission address. `presentations`
  Conferences section expanded to the full call. Added
  `.symposium-box__deadline` and `.symposium-box__links` to
  `styles.scss`. Renamed the PDF Evan dropped in `files/` from
  `call_for_papers_RMIResearchSymposium2027_v08_10_26.pdf` to
  `rmi-research-symposium-2027-cfp.pdf` for a clean public URL.
- **Insurance Tycoon (`61d5c98`, corrected by `4ad6ee7` and `e8987f8`).**
  New Teaching Innovation section on `teaching.qmd` in a gold
  `.feature-entry` box (new in `styles.scss`, full-width sibling of
  `.symposium-box`). First pass also put the sim on `awards` and
  `presentations` and tied it to the Strickler award; Evan corrected
  that — the award was shared with Cassandra R. Cole and Kyeonghee Kim
  for a joint session in which each presenter showed their own work, and
  the simulation is Evan's alone. Final state: sim link on `teaching`
  only, with no award mention; `awards` carries the award with the
  coauthors in parentheses and no sim reference; Aug 2026 ARIA on
  `presentations` is back to the two papers, matching the CV.
- Every change rendered, committed, pushed, published, and verified
  live with `curl`. Pages build confirmed `built` after each publish.
**Output:** `files/cv.pdf`, `files/rmi-research-symposium-2027-cfp.pdf`,
`index.qmd`, `research.qmd`, `teaching.qmd`, `presentations.qmd`,
`service.qmd`, `awards.qmd`, `styles.scss`, `HANDOFF.md`,
`Work/session_progress.md`
**Finding:** A CV refresh carries more site-relevant change than the
"what's new" conversation surfaces. Five of this session's edits came
from diffing the PDF against the pages, not from anything Evan
mentioned — a job title change, a new dissertation chair, two courses,
a paper's status change, and stale scheduling tags. Diff the whole CV
against every page on each new export; don't act only on what gets
mentioned.
**Next:**
1. **RTS History** — the remaining item from this session's list of
   three. Evan expects it to be more involved and wants it started in a
   fresh session, so nothing has been scoped yet. Ask what form it
   should take (a page? a section of `presentations.qmd`? a table of
   past meetings?) before building anything.
2. The August 2026 ARIA Strickler award demonstration is on neither the
   CV nor the site. Worth adding to the CV on the next pass — flagged to
   Evan, his call.
3. The symposium box on `index.qmd` should switch from call-for-papers
   to program details after **September 15, 2026**. A comment in the
   file marks the spot.
4. The Insurance Tycoon link points at a Railway deployment URL
   (`insurance-tycoon-production.up.railway.app`). If the sim moves to a
   custom domain, `teaching.qmd` needs updating.
5. Otherwise unchanged from the 2026-08-07 entry: SSRN backfill for
   published papers #3, 4, 5, 6, 8, 9, 10, 11 and working papers #2,
   5-13; school PC setup; optional photo/`[Slides]`/mobile QA polish.
**Blocked:** None


---

## Session: 2026-08-14 18:03
**Project:** evaneastman-site (Quarto personal website)
**Objective:** Turn the Risk Theory Society publication-tracking
spreadsheet Evan dropped in `files/` into something the website can put
forward. This is the "RTS History" item deferred from the earlier
session, arriving with its own source data rather than as a blank scope
question.
**Completed:**
- **Read the data before proposing anything.** 292 papers across 31
  meetings (1984, then 1994-2024) with up to six author/affiliation
  pairs each, and 37 meetings (1991-2027) with president, host,
  location, and the society's member and attendee counts. Journal
  strings are clean - 68 distinct, no typo variants.
- **The findings that made it worth a page.** About 70% of papers
  through 2019 reach print; median lag from meeting to publication is
  three years (mean 3.5, range -1 to 17), which is what explains the
  recent cohorts rather than any decline. Placement is broad, not
  parochial: JRI leads at 43 but the tail runs through JFE (8), ReStat
  (6), MS (5), JPubE (5), AER (4), Econometrica (3), RAND (2).
  Membership roughly doubled, 59 in 1993 to 107 in 2022.
- **`rts.qmd`, unlisted** (commits `47ce4b1`, `11414e1`, `742c093`).
  Four headline tiles, three hand-rolled SVG
  charts (papers and outcome by year with a censoring band, top
  journals, members vs attendance with real gaps drawn as gaps), a
  searchable and sortable table of all 292 papers with 185 linked
  titles, and the 37-meeting history. Built like `family-tree.qmd`:
  `noindex`, `search: false`, and the existing post-render hook drops
  it from `sitemap.xml` with no change needed to that script.
- **`tools/build-rts-data.py`** extracts the workbook into a marked
  block in the page. Every displayed number - tiles, chart labels, note
  text, and the two figures quoted in the intro prose - is computed
  from that blob at load time, so the page cannot drift from the
  workbook as it gains a meeting a year.
- **`tools/Update-RTS.ps1`** collapses refresh to one command after
  Evan said editing JSON would be worse than Excel. It rebuilds the
  data block and renders. He edits the workbook and nothing else.
- **Verified in the browser, not just rendered.** Search across titles,
  authors, affiliations, and journals; sorting on three columns;
  year filter; published-only toggle; empty state; no page-level
  horizontal overflow at 360px with both tables scrolling internally.
  Console clean (the only errors are the Zotero extension).
- **Two bugs caught by looking at the page.** The 2025 meeting was
  tagged "Upcoming" because I derived that from the last year with
  *papers* (2024) - the meeting happened, its program just is not
  entered yet; it now keys off the last meeting with recorded counts.
  And a 2024 paper published in 2024 read "0 yrs after," now "same
  year."
- **Reversed my own gitignore call.** I first kept the workbook out of
  git to keep raw data off a public repo, then Evan named it his
  standing source of truth. Since `rts.qmd` carries the same 292 rows
  as JSON and is committed, the rule bought almost nothing while
  leaving his canonical file with no history, no backup, and no path to
  the school PC. Now tracked.
**Output:** `rts.qmd`, `tools/build-rts-data.py`, `tools/Update-RTS.ps1`,
`.gitignore`, `HANDOFF.md`, `Work/session_progress.md`
**Finding:** A blank journal is a gap in the record, not a verdict on
the paper - 105 of 292 rows have no publication recorded, and the page
says so in the intro, the cell tooltip, and the notes, because it makes
public claims about named scholars' work. Separately: `files/` is safer
than it looks. Quarto copies only the files a page actually links to,
so `_site/files/` holds four of the six files in `files/` - the
workbook and `profile-original.jpg` never ship. That is why tracking the
workbook does not publish it, and why adding a download link to it later
would be a decision rather than a formatting change.
**Next:**
1. **Evan must run `git add files/RTSPublicationTracking_2025.xlsx`
   himself** - staging it was blocked by the permission classifier
   twice, so the workbook is still untracked. Everything else is
   committed.
2. **Decide whether the RTS page goes public.** It is unlisted so Evan
   can send the URL to RTS leadership first. Note that `git push` alone
   exposes the data: the repo is public and `rts.qmd` carries all 292
   rows. Nothing is pushed yet. To list it: add a navbar entry in
   `_quarto.yml`, drop the `robots` meta and `search: false`.
3. **Workbook gaps**, in rough order of value: the 2025 papers (the
   meeting is recorded with 10 papers but no program - Evan finished
   collection before the 2026 meeting), 1985-1993 (no papers at all),
   the 105 rows with no publication outcome. Also retype the 2021
   `date` cell as text (`April 9-11`); Excel stored it as a real date so
   the build script drops it and warns.
4. Unchanged from the earlier 2026-08-14 entry: symposium box flips from
   CFP to program details after Sept 15 2026; the Aug 2026 ARIA
   Strickler demonstration is on neither CV nor site; Insurance Tycoon
   points at a Railway URL; SSRN backfill; school PC setup.
**Blocked:** Staging the `.xlsx` is blocked by the permission
classifier - needs one command from Evan (see Next #1).
