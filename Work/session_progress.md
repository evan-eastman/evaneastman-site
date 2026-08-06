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
