# Changelog

## 2026-04-01 — Initial Restructuring

Forked from scream314/cicada3301 and rebuilt for AI-assisted cryptanalysis.

### Added
- `CLAUDE.md` — AI onboarding with full puzzle context, rules, and data locations
- `data/gematria_primus.json` — first standalone GP data file on GitHub (29 runes, cross-validated from Taiiwo/cicada and iBotPeaches/cicada_3301)
- `data/solve_status.md` — complete page-by-page status table with section mapping
- `data/runes/` — 75 per-page rune transcription files (from rtkd/iddqd master, alignment-verified against image numbering)
- `data/solved_plaintext.md` — all 19 solved pages in reading order, English only
- `data/ciphers_reference.md` — every cipher technique Cicada has used (314 lines)
- `data/magic_squares.json` — three verified magic squares (5x5/3301, 7x7/1033, 5x5/1033)
- `data/unsolved_analysis.md` — per-section stats, rune counts, frequency analysis, attack priorities (509 lines)
- `data/2012_flow.md`, `2013_flow.md`, `2014_flow.md` — Mermaid puzzle flow diagrams
- `.claude/skills/cicada/` — `/cicada` skill with Python toolkit (translate, sum, vigenere, shift, prime, freq, page)

### Changed
- `README.md` — rewritten with project purpose, fork rationale, full source credits

### Fixed
- Rune page files were off-by-one (rtkd transcription skips title page 00.jpg and chapter page 02.jpg) — realigned all 75 files
- Pages 58-64 were undocumented in the original repo — now have full transcriptions from rtkd/iddqd

### Known Issues
- Page 67's base60 grid is marked "wrong!!!" by the community — may need re-transcription
- Rune counts in unsolved_analysis.md should be re-verified after the alignment fix
- `/tmp` clones of reference repos (rtkd-iddqd, taiiwo-cicada, ibotpeaches-cicada) are ephemeral and may need re-cloning

### Next Steps
See open issues on this repo. Priority order:
1. Section 0.7 cryptanalysis (issue #1) — highest frequency deviation
2. Section 0.9 cryptanalysis (issue #2) — shortest unsolved section
3. Base60 grids investigation (issue #3)
4. Deep web hash (issue #4)
5. 58.2kB outguess investigation (issue #5)
6. Improve /cicada skill (issue #6)
