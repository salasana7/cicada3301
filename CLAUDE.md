# Cicada 3301 — AI-Assisted Liber Primus Analysis

## What This Is
This is a fork of [scream314/cicada3301](https://github.com/scream314/cicada3301), restructured for LLM-assisted cryptanalysis. The original repo is the most comprehensive markdown walkthrough of all Cicada 3301 puzzles (2012-2017) with original binary artifacts.

This fork adds structured data files, machine-readable reference tables, and AI onboarding documentation to enable Claude (or any LLM) to efficiently assist with solving the **Liber Primus** — the 75-page runic manuscript that remains the final unsolved Cicada 3301 puzzle.

## The Goal
Decode **LP2** — 56 unsolved pages (pages 17-72) of the Liber Primus, written in Anglo-Saxon runes encrypted with unknown ciphers.

### What's Solved
- **LP1 (pages 00-16):** All 17 pages decoded. Philosophical text about consciousness, divinity, and self-discovery.
- **Page 73:** "AN END" — contains a deep web hash to find.
- **Page 74:** The Parable — "Like the instar tunneling to the surface, we must shed our own circumferences."
- **Total: 19 of 75 pages solved. 56 remain.**

### The 2016 Hint
The last substantive Cicada message (Jan 2016, PGP-signed) said:
> "Liber Primus is the way. Its words are the map, their meaning is the road, and their numbers are the direction."

## Key Data Files

| File | What It Contains |
|------|-----------------|
| `data/gematria_primus.json` | The Rosetta Stone — 29 runes mapped to letters and prime values. Load this first. |
| `data/solve_status.md` | Which pages are solved, which aren't, what cipher was used, what key |
| `data/runes/` | One file per LP page with raw rune transcription (from rtkd/iddqd master) |
| `data/solved_plaintext.md` | All solved pages in reading order, English only |
| `data/ciphers_reference.md` | Every cipher technique Cicada has used |
| `liber_primus.md` | Original detailed walkthrough of all 75 pages (from upstream) |
| `assets/2014/liber-primus-complete/` | The 75 JPG page images |

## How to Approach Analysis

### The Gematria Primus (data/gematria_primus.json)
29 Anglo-Saxon runes, each mapped to a prime number (2-109). This is the encoding alphabet for everything. Key properties:
- Values are the first 29 primes
- Some runes map to digraphs: ᚦ=TH, ᛇ=EO, ᛝ=NG, ᛟ=OE, ᚫ=AE, ᛡ=IA/IO, ᛠ=EA
- Ambiguous runes: ᚢ=U/V, ᚳ=C/K, ᛋ=S/Z
- Gematria sum = sum of prime values of all runes in a word/line (often yields primes or emirps)

### Ciphers Used on Solved Pages
1. **Direct substitution** — rune → letter via Gematria Primus (pages 00, 02, 05, 10-13, 16, 74)
2. **Reversed Gematria** — inverted rune-to-letter mapping (page 01)
3. **Vigenere** — polyalphabetic with known keys: `DIVINITY`, `FIRFUMFERENFE`, `welcome pilgrim to the` (pages 03-04, 14-15)
4. **Shift cipher** — fixed rotation (e.g., shift 3 down reversed Gematria for pages 06-09)
5. **phi(prime) shift** — Euler's totient of successive primes as key stream (page 73)

### What's Been Tried on Unsolved Pages
- Brute-force Vigenere with various key lengths
- Gematria rotations and key-dragging
- N-gram frequency analysis (shows non-random distribution → IS meaningful ciphertext)
- Hill cipher, Atbash, Autokey, Playfair attempts
- Hashcat against the deep web hash (page 73)
- Community consensus: encryption was at the runic level, not Latin level

### Working Hypotheses
- Prime-Fibonacci sequence integration (seen in 2016/2017 messages)
- Keys may derive from the solved philosophical text
- Single-rune words may represent digraphs (TH, NG, EA), not just single letters (A, I, O)
- The "numbers are the direction" hint may point to Gematria sums as part of the key

## Cipher Notation
In `data/runes/` files and solve_status.md:
- `•` or `-` = word separator
- `.` = clause separator
- `/` = line break (from original page layout)
- `%` = page break

## External Data Sources
This fork incorporates data from the broader Cicada solver community:

| Source | What We Use | URL |
|--------|------------|-----|
| rtkd/iddqd | Master rune transcriptions, keys, translations | https://github.com/rtkd/iddqd |
| Taiiwo/cicada | Gematria Primus mapping, LP text data | https://github.com/Taiiwo/cicada |
| iBotPeaches/cicada_3301 | GP table verification, methodology docs | https://github.com/iBotPeaches/cicada_3301 |
| yo-yo-yo-jbo/cicada_tools | Structured section.json LP data | https://github.com/yo-yo-yo-jbo/cicada_tools |
| cicada-solvers org (53 repos) | Tools, analysis, community data | https://github.com/cicada-solvers |
| CicadaSolvers.com | Quickstart briefing, cryptanalysis notes | https://www.cicadasolvers.com |
| Uncovering Cicada Wiki | Page-by-page analysis, solve history | https://uncovering-cicada.fandom.com |
| relikd/LiberPrayground | Verified rune stream data, solver tools | https://github.com/relikd/LiberPrayground |

## Project History
This fork was created on 2026-04-01 by a researcher investigating whether modern LLMs can contribute to Liber Primus cryptanalysis. As of this date, no LLM has been systematically applied to the unsolved pages — the only prior attempt was a cursory GPT-4 test by Connor Tumbleson (Jan 2024) which produced no novel results.

The restructuring prioritizes making the puzzle data machine-readable and contextually rich so that an AI assistant can load the Gematria Primus, understand what's been tried, and focus compute on what hasn't.

## Rules for AI Assistants
- **NEVER attempt to OCR runes from the JPG images.** GPT-4 tried this (Jan 2024) and hallucinated extra characters due to variable rune box sizes. It does not work. Use the pre-transcribed text files in `data/runes/` instead — they are community-verified and authoritative.
- The Gematria Primus in `data/gematria_primus.json` is the authoritative mapping. Do not guess rune values.
- Check `data/solve_status.md` before working on any page — it may already be solved.
- The rune transcriptions in `data/runes/` come from rtkd/iddqd and are community-verified. Trust them over any other source.
- Pages 66-68 contain base60/decimal number grids, not runes. These may be encoded rune data in a different format.
- PGP signatures in the original markdown files are verification artifacts. Skip them during analysis.
- All Cicada messages are signed with PGP key 7A35090F. Any unsigned message is not from Cicada.
