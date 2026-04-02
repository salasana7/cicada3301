#!/usr/bin/env python3
"""Gematria Primus toolkit for Liber Primus cryptanalysis."""

import json
import math
import os
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
GP_PATH = REPO_ROOT / "data" / "gematria_primus.json"
RUNES_DIR = REPO_ROOT / "data" / "runes"

# Load Gematria Primus
with open(GP_PATH) as f:
    GP_DATA = json.load(f)

RUNES = GP_DATA["runes"]
RUNE_CHARS = [r["rune"] for r in RUNES]
ALPHABET_SIZE = len(RUNES)  # 29

# Lookup tables
RUNE_TO_IDX = {r["rune"]: r["index"] for r in RUNES}
RUNE_TO_LETTERS = {r["rune"]: r["letters"] for r in RUNES}
RUNE_TO_VALUE = {r["rune"]: r["value"] for r in RUNES}
IDX_TO_RUNE = {r["index"]: r["rune"] for r in RUNES}
LETTER_TO_RUNE = {}
for r in RUNES:
    for letter in r["letters"]:
        LETTER_TO_RUNE[letter.upper()] = r["rune"]


def is_rune(ch):
    return ch in RUNE_TO_IDX


def extract_runes(text):
    return [ch for ch in text if is_rune(ch)]


def translate(text):
    """Translate runes to Latin or Latin to runes."""
    runes_in = extract_runes(text)
    if runes_in:
        # Runes to Latin
        result = []
        for ch in text:
            if is_rune(ch):
                letters = RUNE_TO_LETTERS[ch]
                result.append(letters[0])
            else:
                result.append(ch)
        latin = "".join(result)
        print(f"Runes → Latin: {latin}")
        print(f"Rune count: {len(runes_in)}")
        # Also show per-rune breakdown
        print("\nPer-rune:")
        for ch in text:
            if is_rune(ch):
                letters = "/".join(RUNE_TO_LETTERS[ch])
                val = RUNE_TO_VALUE[ch]
                idx = RUNE_TO_IDX[ch]
                print(f"  {ch} → {letters} (value={val}, index={idx})")
    else:
        # Latin to runes
        result = []
        i = 0
        upper = text.upper()
        while i < len(upper):
            matched = False
            # Try digraphs first (TH, NG, ING, EO, OE, AE, IA, IO, EA)
            for length in [3, 2]:
                if i + length <= len(upper):
                    chunk = upper[i:i + length]
                    if chunk in LETTER_TO_RUNE:
                        result.append(LETTER_TO_RUNE[chunk])
                        i += length
                        matched = True
                        break
            if not matched:
                ch = upper[i]
                if ch in LETTER_TO_RUNE:
                    result.append(LETTER_TO_RUNE[ch])
                elif ch == " ":
                    result.append("-")
                else:
                    result.append(ch)
                i += 1
        print(f"Latin → Runes: {''.join(result)}")


def gematria_sum(text):
    """Compute Gematria Primus sum."""
    runes = extract_runes(text)
    if not runes:
        # Try as Latin text
        upper = text.upper()
        total = 0
        i = 0
        while i < len(upper):
            matched = False
            for length in [3, 2]:
                if i + length <= len(upper):
                    chunk = upper[i:i + length]
                    if chunk in LETTER_TO_RUNE:
                        rune = LETTER_TO_RUNE[chunk]
                        total += RUNE_TO_VALUE[rune]
                        i += length
                        matched = True
                        break
            if not matched:
                ch = upper[i]
                if ch in LETTER_TO_RUNE:
                    rune = LETTER_TO_RUNE[ch]
                    total += RUNE_TO_VALUE[rune]
                i += 1
        runes_text = text
    else:
        total = sum(RUNE_TO_VALUE[r] for r in runes)
        runes_text = "".join(runes)

    print(f"Input: {text}")
    print(f"GP Sum: {total}")
    print(f"Is prime: {is_prime(total)}")
    if is_prime(total):
        rev = int(str(total)[::-1])
        if is_prime(rev) and rev != total:
            print(f"Is emirp: True (reversed: {rev})")


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def check_prime(n):
    """Check primality and emirp status."""
    n = int(n)
    print(f"Number: {n}")
    print(f"Is prime: {is_prime(n)}")
    if is_prime(n):
        rev = int(str(n)[::-1])
        if is_prime(rev) and rev != n:
            print(f"Is emirp: True (reversed: {rev} is also prime)")
        else:
            print(f"Is emirp: False")
        # Find position in prime sequence
        count = 0
        candidate = 2
        while candidate <= n:
            if is_prime(candidate):
                count += 1
            candidate += 1
        print(f"Position in prime sequence: {count}")
        if count <= 29:
            rune = IDX_TO_RUNE.get(count - 1)
            if rune:
                print(f"GP rune at this position: {rune} ({'/'.join(RUNE_TO_LETTERS[rune])})")
    # Factorize if composite
    if not is_prime(n) and n > 1:
        factors = factorize(n)
        print(f"Factors: {' × '.join(str(f) for f in factors)}")


def factorize(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def vigenere(rune_text, key, decrypt=False):
    """Vigenere cipher on the GP alphabet."""
    runes = extract_runes(rune_text)
    # Parse key — could be runes, Latin letters, or a word
    key_indices = []
    key_upper = key.upper()
    for ch in key_upper:
        if ch in LETTER_TO_RUNE:
            rune = LETTER_TO_RUNE[ch]
            key_indices.append(RUNE_TO_IDX[rune])
        elif ch in RUNE_TO_IDX:
            key_indices.append(RUNE_TO_IDX[ch])

    if not key_indices:
        print(f"Error: could not parse key '{key}'")
        return

    print(f"Key: {key} → indices {key_indices}")
    print(f"Key length: {len(key_indices)}")
    print(f"Mode: {'decrypt' if decrypt else 'encrypt'}")

    result = []
    key_pos = 0
    for ch in rune_text:
        if is_rune(ch):
            idx = RUNE_TO_IDX[ch]
            k = key_indices[key_pos % len(key_indices)]
            if decrypt:
                new_idx = (idx - k) % ALPHABET_SIZE
            else:
                new_idx = (idx + k) % ALPHABET_SIZE
            result.append(IDX_TO_RUNE[new_idx])
            key_pos += 1
        else:
            result.append(ch)

    output = "".join(result)
    print(f"\nInput:  {rune_text}")
    print(f"Output: {output}")
    # Also show Latin translation
    latin = []
    for ch in output:
        if is_rune(ch):
            latin.append(RUNE_TO_LETTERS[ch][0])
        else:
            latin.append(ch)
    print(f"Latin:  {''.join(latin)}")


def shift_cipher(rune_text, n, reverse=False, down=False):
    """Shift cipher on GP alphabet."""
    result = []
    for ch in rune_text:
        if is_rune(ch):
            idx = RUNE_TO_IDX[ch]
            if reverse:
                idx = ALPHABET_SIZE - 1 - idx
            if down:
                new_idx = (idx - n) % ALPHABET_SIZE
            else:
                new_idx = (idx + n) % ALPHABET_SIZE
            if reverse:
                new_idx = ALPHABET_SIZE - 1 - new_idx
            result.append(IDX_TO_RUNE[new_idx])
        else:
            result.append(ch)

    output = "".join(result)
    print(f"Shift: {n}, reverse={reverse}, down={down}")
    print(f"Input:  {rune_text}")
    print(f"Output: {output}")
    latin = []
    for ch in output:
        if is_rune(ch):
            latin.append(RUNE_TO_LETTERS[ch][0])
        else:
            latin.append(ch)
    print(f"Latin:  {''.join(latin)}")


def freq_analysis(page_num):
    """Frequency analysis on a page or all unsolved pages."""
    if page_num == "all":
        pages = range(25, 73)  # Unsolved pages
    else:
        pages = [int(page_num)]

    all_runes = []
    for p in pages:
        fpath = RUNES_DIR / f"page_{p:02d}.txt"
        if fpath.exists():
            text = fpath.read_text()
            all_runes.extend(extract_runes(text))

    if not all_runes:
        print("No runes found.")
        return

    total = len(all_runes)
    counts = Counter(all_runes)

    print(f"Total runes: {total}")
    print(f"Unique runes: {len(counts)}")
    print()

    # Frequency table
    print(f"{'Rune':<4} {'Letter':<8} {'Count':<8} {'Freq %':<8} {'Expected %':<10}")
    print("-" * 42)
    expected = 100.0 / ALPHABET_SIZE
    for r in RUNE_CHARS:
        c = counts.get(r, 0)
        freq = 100.0 * c / total if total > 0 else 0
        letters = "/".join(RUNE_TO_LETTERS[r])
        print(f"{r:<4} {letters:<8} {c:<8} {freq:<8.2f} {expected:<10.2f}")

    # Entropy
    entropy = 0
    for c in counts.values():
        p = c / total
        if p > 0:
            entropy -= p * math.log2(p)
    max_entropy = math.log2(ALPHABET_SIZE)
    print(f"\nEntropy: {entropy:.4f} bits (max: {max_entropy:.4f})")
    print(f"Entropy ratio: {entropy / max_entropy:.4f}")

    # Index of Coincidence
    ic_num = sum(c * (c - 1) for c in counts.values())
    ic_den = total * (total - 1) if total > 1 else 1
    ic = ic_num / ic_den
    ic_random = 1.0 / ALPHABET_SIZE
    ic_english = 0.0667  # approximate for English
    print(f"\nIndex of Coincidence: {ic:.6f}")
    print(f"  Random (1/29): {ic_random:.6f}")
    print(f"  English (~): {ic_english:.6f}")
    if ic > ic_random * 1.5:
        print("  → Suggests monoalphabetic or short-key cipher")
    else:
        print("  → Suggests polyalphabetic or long-key cipher")


def show_page(page_num):
    """Display a rune page with metadata."""
    p = int(page_num)
    fpath = RUNES_DIR / f"page_{p:02d}.txt"
    if not fpath.exists():
        print(f"Page {p:02d} not found.")
        return

    text = fpath.read_text()
    runes = extract_runes(text)
    words = [w for w in text.split("-") if extract_runes(w)]

    print(text)
    print(f"\nStats:")
    print(f"  Rune count: {len(runes)}")
    print(f"  Word count: {len(words)}")
    print(f"  GP sum: {sum(RUNE_TO_VALUE[r] for r in runes)}")
    gp_sum = sum(RUNE_TO_VALUE[r] for r in runes)
    print(f"  GP sum is prime: {is_prime(gp_sum)}")


def main():
    if len(sys.argv) < 2:
        print("Usage: gematria.py <command> [args]")
        print("Commands: translate, sum, vigenere, prime, freq, page, shift")
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "translate":
        translate(" ".join(sys.argv[2:]))
    elif cmd == "sum":
        gematria_sum(" ".join(sys.argv[2:]))
    elif cmd == "prime":
        check_prime(sys.argv[2])
    elif cmd == "vigenere":
        rune_text = sys.argv[2]
        key = None
        decrypt = False
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--key":
                key = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--decrypt":
                decrypt = True
                i += 1
            else:
                i += 1
        if key is None:
            print("Error: --key required")
            sys.exit(1)
        vigenere(rune_text, key, decrypt)
    elif cmd == "shift":
        rune_text = sys.argv[2]
        n = 0
        reverse = False
        down = False
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--n":
                n = int(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] == "--reverse":
                reverse = True
                i += 1
            elif sys.argv[i] == "--down":
                down = True
                i += 1
            else:
                i += 1
        shift_cipher(rune_text, n, reverse, down)
    elif cmd == "freq":
        freq_analysis(sys.argv[2] if len(sys.argv) > 2 else "all")
    elif cmd == "page":
        show_page(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
