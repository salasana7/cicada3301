<p align="middle"><img src="assets/2012/cicada.jpg" alt="cicada.jpg" width="600" border="2"></p>

# Cicada 3301 — AI-Assisted Liber Primus Analysis

## What Is This?

This is a fork of [scream314/cicada3301](https://github.com/scream314/cicada3301) — the most comprehensive single-repo archive of the [Cicada 3301](https://en.wikipedia.org/wiki/Cicada_3301) puzzle series (2012-2017). The original repo contains detailed markdown walkthroughs of every puzzle year plus ~200MB of original binary artifacts: the 75 Liber Primus page images, audio files, Tor hidden service snapshots, outguess extractions, and more.

This fork restructures that archive for **AI-assisted cryptanalysis** of the Liber Primus — the 75-page runic manuscript that remains the final unsolved Cicada 3301 puzzle.

## Why This Exists

Of the 75 runic pages in the Liber Primus, **56 remain unsolved** after 12+ years of community effort. The last confirmed PGP-signed Cicada message (January 2016) said:

> *"Liber Primus is the way. Its words are the map, their meaning is the road, and their numbers are the direction."*

Despite an active solver community (the [CicadaSolvers Discord](https://discord.com/channels/572330844056715284/) has thousands of members, there was a [DEF CON 31 presentation](https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20presentations/) on it in 2023, and tools are still being built in 2026), no new pages have been cracked since the initial solve wave. As of April 2026, no LLM has been systematically applied to the unsolved pages — the only prior attempt was a [cursory GPT-4 test](https://connortumbleson.com/2024/01/29/ai-cicada-3301/) by Connor Tumbleson in January 2024, which produced no novel results.

This project asks: can modern LLMs contribute to cryptanalysis if given properly structured data?

## Why a Fork?

We considered starting from scratch, but the original [scream314/cicada3301](https://github.com/scream314/cicada3301) repo contains irreplaceable assets that took years to collect — 75 Liber Primus JPGs, outguess extractions, audio files, Tor service snapshots, CicadaOS contents, and detailed walkthroughs cross-referencing all of it. Rebuilding that would be pointless duplication.

Instead, we keep the `assets/` directory and original documentation untouched, and add a `data/` layer on top with machine-readable structured files that an LLM can actually work with. The original markdown files are great for human researchers; the new data files are optimized for AI consumption.

## What We Built

**See [CLAUDE.md](CLAUDE.md) for AI assistant onboarding instructions.**

### Structured Data
| File | Description |
|------|-------------|
| [CLAUDE.md](CLAUDE.md) | AI onboarding: what to load first, how to approach analysis |
| [data/gematria_primus.json](data/gematria_primus.json) | The Rosetta Stone: 29 runes mapped to letters and prime values (JSON) — the first standalone GP data file on GitHub |
| [data/solve_status.md](data/solve_status.md) | Which pages are solved/unsolved, what cipher, what key |
| [data/runes/](data/runes/) | 75 individual rune transcription files (one per LP page, aligned to image numbering) |
| [data/solved_plaintext.md](data/solved_plaintext.md) | All 19 solved pages in reading order, English only |
| [data/ciphers_reference.md](data/ciphers_reference.md) | Every cipher technique Cicada has used, with keys and parameters |
| [data/magic_squares.json](data/magic_squares.json) | Three magic squares (5x5/3301, 7x7/1033, 5x5/1033) in structured format |
| [data/unsolved_analysis.md](data/unsolved_analysis.md) | Per-section stats, rune counts, frequency analysis, attack priorities |

### Puzzle Flow Diagrams (Mermaid)
| File | Description |
|------|-------------|
| [data/2012_flow.md](data/2012_flow.md) | 2012 puzzle: 4chan → OutGuess → book codes → GPS coordinates → Tor |
| [data/2013_flow.md](data/2013_flow.md) | 2013 puzzle: Book of Law → CicadaOS → Twitter XOR → Gematria Primus |
| [data/2014_flow.md](data/2014_flow.md) | 2014 puzzle: 7 onion services → magic squares → Liber Primus delivery |

### Tooling
| File | Description |
|------|-------------|
| [.claude/skills/cicada/](.claude/skills/cicada/) | `/cicada` skill for Claude Code: translate runes, compute GP sums, Vigenere encrypt/decrypt, primality checks, frequency analysis |

---

## Acknowledgments and Sources

This project stands on the shoulders of over a decade of community work. None of the cryptanalysis knowledge, rune transcriptions, or puzzle documentation originated here — we organized and restructured it for AI consumption.

### The Foundation
- **[scream314/cicada3301](https://github.com/scream314/cicada3301)** — The upstream repo this fork is built on. The most complete single-repo Cicada 3301 archive, with detailed walkthroughs and original binary artifacts.

### Rune Transcriptions and Data
- **[rtkd/iddqd](https://github.com/rtkd/iddqd)** (188 stars) — The gold-standard community transcription of all 75 Liber Primus pages. Our `data/runes/` files are split from their master transcription. Also contains sentence-segmented transcriptions, known translations, cipher keys, and a TTF rune font.
- **[Taiiwo/cicada](https://github.com/Taiiwo/cicada)** (18 stars) — Python library with programmatic access to the LP text and Gematria Primus mapping. Our `gematria_primus.json` was cross-validated against their `gematria.py`.
- **[iBotPeaches/cicada_3301](https://github.com/iBotPeaches/cicada_3301)** (25 stars, updated March 2026) — Comprehensive solving toolkit with a Gematria Primus markdown table we used for cross-validation. Connor Tumbleson's [blog series](https://connortumbleson.com/2021/02/15/the-cicada-3301-mystery-puzzle-3-part1/) (4 parts, 2021-2024) is the best documented walkthrough of the 2014 puzzle.

### Community Tools and Analysis
- **[cicada-solvers](https://github.com/cicada-solvers)** (53 repos) — The community GitHub organization. Notable repos: [lp-decrypter](https://github.com/cicada-solvers/lp-decrypter) (brute-force decrypter with GUI), [libergo](https://github.com/cicada-solvers/libergo) (50+ Go CLI tools), [cmbcidada3301](https://github.com/cicada-solvers/cmbcidada3301) (.NET desktop analysis app), [GematriaPrimusTool](https://github.com/cicada-solvers/GematriaPrimusTool) (web translator).
- **[relikd/LiberPrayground](https://github.com/relikd/LiberPrayground)** — Double-checked rune stream data and Python solving tools (Vigenere, Affine, Autokey).
- **[yo-yo-yo-jbo/cicada_tools](https://github.com/yo-yo-yo-jbo/cicada_tools)** — Structured `section.json` LP data per chapter, transformer pipeline architecture.

### Knowledge Bases
- **[Uncovering Cicada Wiki](https://uncovering-cicada.fandom.com/)** — The definitive community reference. Page-by-page LP analysis, solve history, Gematria Primus table.
- **[CicadaSolvers.com](https://www.cicadasolvers.com)** — Quickstart briefing, LP viewer, cryptanalysis notes, community tools.
- **[CicadaSolvers Discord](https://discord.com/channels/572330844056715284/)** — Active community with thousands of members and regular voice sessions.

### Historical Documentation
- **[DEF CON 31 presentation](https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20presentations/)** (Aug 2023) — "Cracking Cicada 3301: The Future of Collaborative Puzzle-Solving" by Taiiwo, Artorias, Puck, TheClockworkBird.
- **[Connor Tumbleson's AI & Cicada 3301](https://connortumbleson.com/2024/01/29/ai-cicada-3301/)** (Jan 2024) — The only documented attempt to apply an LLM (GPT-4) to Cicada puzzles.
- **[micheloosterhof/cicada-2014](https://github.com/micheloosterhof/cicada-2014)** and **[cicada-2016](https://github.com/micheloosterhof/cicada-2016)** — Year-specific puzzle archives.
- **[bibanon wiki](https://github.com/bibanon/bibanon/wiki/Cicada-3301-wiki)** — Additional community documentation.

---

## Original Content

The original upstream content is preserved in full below.

Almost all original files are under [assets/](assets/) sorted by year. The full Liber Primus images are [here](assets/2014/liber-primus-complete).

### Years
 * [2012](2012.md) - [map](2012.png)
 * [2013](2013.md) - [map](2013.png)
 * [2014](2014.md) - [map](2014.png)
 * [2015](2015.md)
 * [2016](2016.md)
 * [2017](2017.md)

### Others
  * [gematria primus](gematria_primus.md)
  * [irl addresses](irl.md)
  * [pages and ciphers](pages_and_ciphers.md)
  * [liber primus](liber_primus.md)
  * [possible hints, never used](hints_never_used.md)
