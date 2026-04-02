---
name: cicada
description: Gematria Primus tools for Liber Primus cryptanalysis — transliterate runes, compute sums, decrypt ciphers, check primes
allowed-tools: Read, Bash
argument-hint: "<command> [args] — try: translate, sum, vigenere, prime, freq, page"
---

# Cicada 3301 Cryptanalysis Toolkit

You are assisting with cryptanalysis of the unsolved Liber Primus pages. Use the Python helper at `.claude/skills/cicada/scripts/gematria.py` for all operations.

## Available Commands

When the user invokes `/cicada`, parse `$ARGUMENTS` and run the appropriate command:

### translate <runes or text>
Convert runes to Latin letters or Latin text to runes.
```bash
python3 .claude/skills/cicada/scripts/gematria.py translate "ᚠᛁᚾᛞ"
```

### sum <runes or text>
Compute the Gematria Primus sum (sum of prime values) of the input.
```bash
python3 .claude/skills/cicada/scripts/gematria.py sum "ᚠᛁᚾᛞ"
```

### vigenere <runes> --key <key> [--decrypt]
Apply Vigenere cipher on the Gematria Primus alphabet. Default encrypts; use --decrypt to reverse.
```bash
python3 .claude/skills/cicada/scripts/gematria.py vigenere "ᚢᛠᛝᛋᛇᚠᚳ" --key DIVINITY --decrypt
```

### prime <number>
Check if a number is prime, and if so, whether it's an emirp (prime when reversed).
```bash
python3 .claude/skills/cicada/scripts/gematria.py prime 3301
```

### freq <page_number or "all">
Run frequency analysis on a page or all unsolved pages. Shows rune distribution, entropy, and Index of Coincidence.
```bash
python3 .claude/skills/cicada/scripts/gematria.py freq 25
python3 .claude/skills/cicada/scripts/gematria.py freq all
```

### page <page_number>
Load and display a rune page with its metadata (section, solve status, rune/word counts).
```bash
python3 .claude/skills/cicada/scripts/gematria.py page 25
```

### shift <runes> --n <shift_amount> [--reverse] [--down]
Apply a shift cipher on the GP alphabet. Flags control direction.
```bash
python3 .claude/skills/cicada/scripts/gematria.py shift "ᚹ-ᚣᛠᚹᛟ" --n 3 --reverse --down
```

## Context
- The Gematria Primus mapping is at `data/gematria_primus.json`
- Rune transcriptions are at `data/runes/page_XX.txt`
- Solve status is at `data/solve_status.md`
- Full analysis notes at `data/unsolved_analysis.md`
- Recommended attack order: Section 0.7 (pages 25-31) first, then 0.9 (pages 40-43)

## Important Notes
- The GP alphabet has 29 runes. All arithmetic is mod 29.
- F (ᚠ) is sometimes left unencrypted in Vigenere ciphers ("F unencrypted" rule).
- Word separators are `•` or `-`. Clause separators are `.`. Line breaks are `/`.
- If the user provides raw rune text without a command, default to `translate`.
