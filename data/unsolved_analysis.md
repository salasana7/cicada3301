# Unsolved Liber Primus Pages -- Comprehensive Analysis

Generated: 2026-04-01
Purpose: Go-to reference for any session starting cryptanalysis on the unsolved LP2 pages.

---

## 1. Summary Statistics

| Metric | Value |
|--------|-------|
| Total unsolved pages (0.7--0.12) | 48 (pages 25--72) |
| Total rune characters | 10,739 |
| Total rune-words | 2,772 |
| Average runes per page | 223.7 |
| Average words per page | 57.8 |
| Unique rune types used | 29/29 (full Gematria Primus alphabet) |
| Pages with number grids instead of runes | 3 (pages 64--65 partial, 66 partial) |
| Pages with base60 number grids | 3 (pages 64--65--66, spanning into pages 67--68 content) |
| Pages with outguess 58.2kB garbage | 8 (pages 17, 21, 43, 65, 68, 69, 70, 71) |

### Key Caveat: Pages 71--72 Data Integrity Issue

The rune transcription files `page_71.txt` and `page_72.txt` contain content identical to `page_73.txt` (AN END, solved) and `page_74.txt` (A PARABLE, solved) respectively. However, the upstream `liber_primus.md` shows that 71.jpg contains different encrypted content beginning with `ᚪ-ᛗᛝᛞᛡᚦᛉᛁᛗ` ("A MIDPOINT" encrypted subsection title) followed by a large block of encrypted runes. The rune files for pages 71 and 72 need to be corrected against the upstream source before cryptanalysis of these pages.

The rune counts and word counts below include the current (incorrect) page_71.txt and page_72.txt data. The true unsolved rune count for section 0.12 is higher than reported here once the correct 71.jpg transcription is used.

---

## 2. Per-Section Breakdown

### Section 0.7 -- Pages 25--31 (7 pages)

| Metric | Value |
|--------|-------|
| Total runes | 1,632 |
| Total words | 421 |
| Content lines | 79 |
| Unique runes | 29/29 |

**Per-page counts:**

| Page | Runes | Words | Lines | Notes |
|------|-------|-------|-------|-------|
| 25 | 263 | 73 | 12 | Contains "7" (digit) embedded in rune text |
| 26 | 273 | 62 | 12 | |
| 27 | 261 | 72 | 12 | |
| 28 | 272 | 69 | 12 | |
| 29 | 137 | 34 | 7 | Short page -- section end marker `&` `$` |
| 30 | 159 | 42 | 12 | **Number grid** (4x4): 3258/3222/3152/3038 / 3278/3299/3298/2838 / 3288/3294/3296/2472 / 4516/1206/708/1820. Followed by rune text. Title runes: `ᚠᚢᛚᛗ-ᚪᛠᚣᛟᚪ` |
| 31 | 267 | 69 | 12 | |

**Outguess status:** No 58.2kB garbage output found on any page in this section.

**Known cribs:** None established. The section title is encrypted.

**Special content:** Page 30 has a 4x4 number grid before the rune text. The grid values (708--4516) are significantly larger than Gematria Primus values (2--109), suggesting they may be gematria sums of words/phrases, or encoded differently. The rune header `ᚠᚢᛚᛗ-ᚪᛠᚣᛟᚪ` precedes the grid and may be a section/subsection title.

**Frequency analysis:**
- Entropy: 4.840 bits (ratio to max: 0.9962)
- Chi-squared from uniform: 42.0 (df=28)
- Most frequent: ᛉ(X)=4.7%, ᚢ(U)=4.5%, ᛡ(IA)=4.3%
- Least frequent: ᛄ(J)=2.5%, ᚱ(R)=2.8%, ᛗ(M)=2.8%
- Slightly higher deviation from uniform than other sections, suggesting either a simpler cipher or shorter key length.

---

### Section 0.8 -- Pages 32--39 (8 pages)

| Metric | Value |
|--------|-------|
| Total runes | 1,960 |
| Total words | 509 |
| Content lines | 88 |
| Unique runes | 29/29 |

**Per-page counts:**

| Page | Runes | Words | Lines | Notes |
|------|-------|-------|-------|-------|
| 32 | 273 | 79 | 12 | solve_status says "contains number grid" but rune file is pure runes. The grid is on page 30 (section 0.7). Upstream liber_primus.md shows page 32.jpg has both a number grid header AND rune text as a combined page. |
| 33 | 260 | 68 | 12 | |
| 34 | 271 | 74 | 12 | |
| 35 | 269 | 71 | 12 | |
| 36 | 273 | 60 | 12 | |
| 37 | 131 | 32 | 6 | Short page -- possible section/subsection break |
| 38 | 213 | 52 | 10 | |
| 39 | 270 | 73 | 12 | |

**Outguess status:** No 58.2kB garbage output found on any page in this section.

**Known cribs:** None established.

**Special content:** The number grid associated with page 32 in solve_status is actually from page 30 (see section 0.7 above). The upstream liber_primus.md shows page 32.jpg has a header `ᚠᚢᛚᛗ-ᚪᛠᚣᛟᚪ` followed by a 4x4 grid (3258/3222/3152/3038...) PLUS the rune text that continues. The rune file page_32.txt contains only the rune text portion.

**Frequency analysis:**
- Entropy: 4.851 bits (ratio to max: 0.9987)
- Chi-squared from uniform: 17.4 (df=28) -- **closest to uniform of all sections**
- Most frequent: ᚦ(TH)=4.0%, ᚩ(O)=3.9%, ᛡ(IA)=3.9%
- Least frequent: ᛇ(EO)=2.8%, ᛉ(X)=3.0%, ᚻ(H)=3.0%
- Near-uniform distribution is consistent with a polyalphabetic cipher (e.g., Vigenere) with a long key.

---

### Section 0.9 -- Pages 40--43 (4 pages)

| Metric | Value |
|--------|-------|
| Total runes | 1,041 |
| Total words | 259 |
| Content lines | 47 |
| Unique runes | 29/29 |

**Per-page counts:**

| Page | Runes | Words | Lines | Notes |
|------|-------|-------|-------|-------|
| 40 | 273 | 66 | 12 | |
| 41 | 265 | 69 | 12 | |
| 42 | 234 | 57 | 11 | |
| 43 | 269 | 67 | 12 | **Outguess: 58.2kB garbage** |

**Outguess status:** Page 43 yields 58.2kB garbage output. This is the last page of the section.

**Known cribs:** None established.

**Special content:** None. Pure rune text.

**Frequency analysis:**
- Entropy: 4.835 bits (ratio to max: 0.9953)
- Chi-squared from uniform: 31.9 (df=28)
- Most frequent: ᛠ(EA)=4.6%, ᛒ(B)=4.3%, ᚪ(A)=4.3%
- Least frequent: ᛇ(EO)=2.3%, ᚫ(AE)=2.4%, ᚹ(W)=2.5%
- Highest deviation from uniform among the mid-sections. With only 4 pages, sample size is smallest.

---

### Section 0.10 -- Pages 44--49 (6 pages)

| Metric | Value |
|--------|-------|
| Total runes | 1,405 |
| Total words | 376 |
| Content lines | 65 |
| Unique runes | 29/29 |

**Per-page counts:**

| Page | Runes | Words | Lines | Notes |
|------|-------|-------|-------|-------|
| 44 | 277 | 79 | 12 | Highest rune count of any unsolved page |
| 45 | 263 | 67 | 12 | |
| 46 | 269 | 72 | 12 | |
| 47 | 121 | 26 | 6 | Short page -- section/subsection break |
| 48 | 214 | 61 | 11 | |
| 49 | 261 | 71 | 12 | |

**Outguess status:** No 58.2kB garbage output found on any page in this section.

**Known cribs:** None established.

**Special content:** None. Pure rune text.

**Frequency analysis:**
- Entropy: 4.848 bits (ratio to max: 0.9980)
- Chi-squared from uniform: 18.8 (df=28)
- Most frequent: ᚹ(W)=4.4%, ᛞ(D)=4.3%, ᚪ(A)=3.8%
- Least frequent: ᚾ(N)=2.6%, ᚳ(C/K)=2.7%, ᛠ(EA)=3.0%
- Close to uniform, consistent with polyalphabetic cipher.

---

### Section 0.11 -- Pages 50--56 (7 pages)

| Metric | Value |
|--------|-------|
| Total runes | 1,709 |
| Total words | 437 |
| Content lines | 80 |
| Unique runes | 29/29 |

**Per-page counts:**

| Page | Runes | Words | Lines | Notes |
|------|-------|-------|-------|-------|
| 50 | 271 | 71 | 12 | solve_status says "contains number grid" -- see note below |
| 51 | 238 | 58 | 11 | |
| 52 | 228 | 60 | 11 | |
| 53 | 228 | 53 | 11 | |
| 54 | 240 | 64 | 12 | |
| 55 | 231 | 63 | 11 | |
| 56 | 273 | 68 | 12 | |

**Outguess status:** No 58.2kB garbage output found on any page in this section.

**Known cribs:** None established.

**Special content:** Page 50 is noted in solve_status as containing a number grid, but the rune file `page_50.txt` contains only standard rune text. The number grid may be embedded in the JPG image but not transcribed into the rune file, or it may be a section header (like page 30/32) that was separated during transcription.

**Frequency analysis:**
- Entropy: 4.845 bits (ratio to max: 0.9974)
- Chi-squared from uniform: 30.0 (df=28)
- Most frequent: ᛟ(OE)=4.4%, ᛁ(I)=4.4%, ᚪ(A)=4.0%
- Least frequent: ᚠ(F)=2.7%, ᛇ(EO)=2.8%, ᚹ(W)=2.8%
- Note ᚠ(F) is the least frequent rune. In solved Vigenere pages, cleartext F appears as unencrypted ᚠ. If the same F-skipping rule applies here, low ᚠ frequency could mean few F's in the plaintext (expected for English) -- which would support a Vigenere hypothesis.

---

### Section 0.12 -- Pages 57--72 (16 pages) -- LARGEST UNSOLVED BLOCK

| Metric | Value |
|--------|-------|
| Total runes | 2,992 (see caveat about pages 71--72) |
| Total words | 770 |
| Content lines | 174 |
| Unique runes | 29/29 |

**Per-page counts:**

| Page | Runes | Words | Lines | Notes |
|------|-------|-------|-------|-------|
| 57 | 272 | 68 | 12 | Start of section |
| 58 | 274 | 69 | 12 | rtkd/iddqd only -- missing from scream314 docs |
| 59 | 273 | 65 | 12 | rtkd/iddqd only |
| 60 | 270 | 70 | 12 | rtkd/iddqd only |
| 61 | 270 | 71 | 12 | rtkd/iddqd only |
| 62 | 274 | 66 | 12 | rtkd/iddqd only |
| 63 | 271 | 74 | 12 | rtkd/iddqd only |
| 64 | 66 | 20 | 13 | **Mixed content:** 3 lines of runes + 10x8 base60 number grid |
| 65 | 0 | 0 | 13 | **Pure number grid** (13x8 base60). No runes. Outguess: 58.2kB garbage |
| 66 | 92 | 23 | 13 | **Mixed content:** 9x8 base60 grid + 4 lines of runes |
| 67 | 263 | 70 | 12 | Standard rune text |
| 68 | 179 | 46 | 9 | Rune text, shorter page. **Outguess: 58.2kB garbage** |
| 69 | 232 | 58 | 11 | **Outguess: 58.2kB garbage** |
| 70 | 76 | 19 | 4 | Very short page. **Outguess: 58.2kB garbage** |
| 71 | 85 | 28 | 10 | **DATA INTEGRITY ISSUE** -- see below. **Outguess: 58.2kB garbage** |
| 72 | 95 | 23 | 5 | **DATA INTEGRITY ISSUE** -- see below |

**Outguess status:** Pages 65, 68, 69, 70, 71 all yield 58.2kB garbage. This is the densest cluster of outguess-active pages in the entire Liber Primus. Page 72 yields nothing.

**Known cribs:** None established for the encrypted text. However:
- Page 72 rune file contains plaintext "PARABLE.LIKE THE INSTAR TUNNELING TO THE SURFACE..." which is actually page 74's solved content (default GP substitution).
- Page 71 rune file contains "AN END" content (page 73, solved with phi(prime) shift).

---

## 3. Section 0.12 Deep Dive

### Pages 58--64: The Undocumented Block

Pages 58--64 were previously undocumented in the scream314/cicada3301 walkthrough. Their rune transcriptions come exclusively from the rtkd/iddqd master transcription. This means:
- They have had less community scrutiny than other pages
- No per-page outguess analysis exists for pages 58--64 in the upstream docs
- The transcriptions should be verified against the original JPG images

Pages 57--63 are dense, full-length rune pages (~270 runes each, 12 lines). Page 64 transitions abruptly to a base60 number grid after only 3 lines of runes.

### Pages 64--66: The Base60 Number Grids

Three pages contain base60-encoded number grids instead of (or in addition to) runes:

**Page 64:** 3 lines of runes (66 rune characters, 20 words) followed by a 10x8 grid of base60 values.
```
3N-3p-2l-36-1b-3v-26-33
1W-49-2a-3g-47-04-33-3W
21-3M-0F-0X-1g-2H-0x-1R
...
```

**Page 65:** Pure 13x8 base60 grid, no runes at all. This is the only page in the entire Liber Primus with zero rune characters.
```
2M-0w-3L-3D-2r-0S-1p-15
3V-3e-3I-0n-3u-1O-0u-0Z
...
```

**Page 66:** 9x8 base60 grid followed by 4 lines of runes (92 rune characters, 23 words).
```
28-2a-0J-1L-0c-3C-2o-0X
00-2Z-2d-1T-2u-1t-1j-0l
...
```
Followed by rune text: `ᚹᚹᛈ-ᚠᛡᛚᛉᛒᚾ-ᚳᛗᚾᚱᛗ-ᚻᚦᚫᛞᛄ...`

The upstream liber_primus.md provides decimal conversions for pages 66 and 68 (from base60 to decimal, values 0--255 = byte range). Page 67's base60 grid is explicitly marked "wrong!!!" in the upstream source, suggesting a known transcription error.

**Grid dimensions:**
- Page 64 (labeled 66.jpg in upstream): 10 rows x 8 columns = 80 values
- Page 65 (labeled 67.jpg): 13 rows x 8 columns = 104 values
- Page 66 (labeled 68.jpg): 9 rows x 8 columns = 72 values
- Total: 256 values across three grids

**256 total values is significant** -- it is exactly the size of a byte-addressed lookup table, a full ASCII/byte permutation, or the output of a hash function. The decimal values (0--255 range) reinforce this. These grids likely encode either:
1. A substitution table or S-box for decrypting adjacent rune pages
2. Rune text encoded as Gematria Primus values in an alternate format
3. Binary data (a key, a program, or steganographic payload)

### Page 71: "A MIDPOINT" (Encrypted Subsection)

The solve_status notes page 71 has a subsection titled "A MIDPOINT." The upstream liber_primus.md (71.jpg) shows:
- Title line: `ᚪ-ᛗᛝᛞᛡᚦᛉᛁᛗ` (which via default GP substitution reads "A MIDPOINTH" -- close to "A MIDPOINT" with a trailing H likely from rune ᛗ being M and layout artifacts)
- A large block of encrypted rune text
- The hex hash: `36367763ab73783c7af284446c...` (same hash as page 73's "AN END")
- A closing block of encrypted runes

**CRITICAL:** The rune file `page_71.txt` does NOT contain the actual page 71 content. It instead contains an exact copy of page 73's (AN END) rune data. The true page 71 rune data must be extracted from the upstream liber_primus.md or the rtkd/iddqd source before working on this page.

### Page 72: The Parable (Cleartext?)

Page 72's rune file contains what appears to be default GP substitution reading "PARABLE.LIKE THE INSTAR TUNNELING TO THE SURFACE.WE MUST SHED OUR OWN CIRCUMFERENCES.FIND THE DIVINITY WITHIN AND EMERGE." This is identical to page 74 (solved). The upstream liber_primus.md shows 72.jpg has no separate rune transcription, only outguess: none. This suggests page 72 may actually be a blank/separator page, or the rune file was incorrectly populated.

---

## 4. Observations for Cryptanalysis

### 4.1 Frequency Distribution: Remarkably Uniform

All six unsolved sections show rune frequency distributions extremely close to uniform (entropy ratios 0.9953--0.9988 of maximum). This is the signature of a strong polyalphabetic cipher.

| Section | Runes | Entropy Ratio | Chi-sq (df=28) | Assessment |
|---------|-------|---------------|----------------|------------|
| 0.7 | 1,632 | 0.9962 | 42.0 | Slight deviation -- shorter key? |
| 0.8 | 1,960 | 0.9987 | 17.4 | **Most uniform** -- long key or running key |
| 0.9 | 1,041 | 0.9953 | 31.9 | Highest deviation (but smallest sample) |
| 0.10 | 1,405 | 0.9980 | 18.8 | Very uniform |
| 0.11 | 1,709 | 0.9974 | 30.0 | Moderate deviation |
| 0.12 | 2,992 | 0.9988 | 24.9 | Very uniform (largest sample) |

For comparison, natural English mapped through direct GP substitution would produce highly non-uniform frequencies (E, T, A dominating). The near-uniformity across all sections strongly suggests:
1. Every unsolved section uses a polyalphabetic cipher (Vigenere-family or autokey)
2. Key lengths are at least moderate (5+ runes) to produce this level of flattening
3. A running-key cipher (using another text as key) cannot be ruled out

### 4.2 Sections That Might Share a Cipher

**Strong grouping candidates:**

- **Sections 0.8 and 0.10** have the lowest chi-squared values (17.4 and 18.8), suggesting they may use the same cipher type with comparable key lengths. Both are pure rune text with no special content.

- **Sections 0.7 and 0.9** both have higher chi-squared values (42.0 and 31.9). Section 0.7 has a number grid on page 30; section 0.9 has outguess data on page 43. These might use a simpler cipher variant.

- **Sections 0.11 and 0.12** both show ᚠ(F) as one of the least frequent runes (2.7% and 3.9% respectively). If the F-skipping rule from solved Vigenere pages applies, this pattern would be expected.

**Within section 0.12,** the content splits into three distinct types:
1. Dense rune pages (57--63, 67--70): Standard ciphertext
2. Base60 number grids (64--66): Different encoding
3. Structural pages (71--72): Section markers, possibly cleartext/solved

Pages 57--63 and 67--70 likely share a single cipher key. The base60 grids (64--66) are a separate puzzle-within-a-puzzle.

### 4.3 Short Pages as Section Markers

Several pages are notably shorter than the ~270-rune norm:

| Page | Runes | Section | Position |
|------|-------|---------|----------|
| 29 | 137 | 0.7 | End of section (has `&` `$` markers) |
| 37 | 131 | 0.8 | Mid-section -- subsection break? |
| 47 | 121 | 0.10 | Mid-section -- subsection break? |
| 64 | 66 | 0.12 | Transition to base60 grids |
| 70 | 76 | 0.12 | Short, followed by "A MIDPOINT" |

Pages 37 and 47 are likely subsection boundaries within their respective sections. In the solved LP, subsections often have short ending pages. This means sections 0.8 and 0.10 may each contain TWO cipher runs with potentially different keys:
- Section 0.8: pages 32--37 (subsection A) + pages 38--39 (subsection B)
- Section 0.10: pages 44--47 (subsection A) + pages 48--49 (subsection B)

### 4.4 The Recurring 58.2kB Outguess Garbage

Eight JPG images yield exactly 58.2kB of "garbage" when processed with outguess:

| Page | Section | Position in Section |
|------|---------|-------------------|
| 17 | 0.5 | First page of section (solved) |
| 21 | 0.6 | Mid-section (partially solved) |
| 43 | 0.9 | Last page of section |
| 65 | 0.12 | Pure base60 grid page |
| 68 | 0.12 | End of base60 block |
| 69 | 0.12 | After base60 block |
| 70 | 0.12 | Short page before "A MIDPOINT" |
| 71 | 0.12 | "A MIDPOINT" page |

**Observations:**
1. The identical file size (58.2kB = ~59,596 bytes) across all eight pages is almost certainly not coincidence. If this were random JPEG steganographic noise, sizes would vary with the image.
2. The 58.2kB output is consistently called "garbage" -- meaning it does not begin with a PGP header, does not decode as UTF-8 text, and has no recognizable structure.
3. Six of the eight pages are in section 0.12 (pages 65, 68, 69, 70, 71), heavily concentrated in the second half of the section. Only pages 17, 21, and 43 are outside section 0.12.
4. Page 17 (section 0.5) is solved -- the outguess data there has never been explained. If the 58.2kB data on page 17 could be analyzed (it's presumably available from the JPG), it could serve as a known-context reference for the other seven.

**Hypotheses for the 58.2kB data:**
- **Encrypted payload:** The data may be encrypted with a key derived from the rune text (solve the runes first, then decrypt the steganographic data).
- **Concatenation required:** The eight 58.2kB blocks may need to be concatenated or XOR'd together. 8 x 58.2kB ~ 466kB could contain a substantial hidden message or even a program.
- **Red herring / padding:** Outguess can produce false positive extractions from JPEG images. However, identical sizes argue against random false positives.
- **Shared symmetric key:** All eight may be encrypted with the same key, which would be revealed by solving a particular page.

### 4.5 The ᛇ (EO) Anomaly

Across all unsolved sections, ᛇ (EO, value=41) is consistently the least or near-least frequent rune:

| Section | ᛇ(EO) Rank | ᛇ(EO) % |
|---------|------------|----------|
| 0.7 | 27th/29 | 2.8% |
| 0.8 | 29th/29 | 2.8% |
| 0.9 | 29th/29 | 2.3% |
| 0.10 | (not in bottom 5) | ~3.3% |
| 0.11 | 28th/29 | 2.8% |
| 0.12 | (not in bottom 5) | ~3.0% |
| **Global** | **29th/29** | **3.0%** |

In a perfect polyalphabetic cipher over 29 symbols, each should appear ~3.45%. ᛇ consistently appears below expected. This could indicate:
- A systematic bias in the cipher (perhaps the cipher avoids certain rune positions)
- A structural property of the plaintext combined with the cipher
- Or simply statistical fluctuation (3.0% vs 3.45% is small)

### 4.6 Digit "7" on Page 25

Page 25 contains the digit `7` embedded in the rune text: `ᚩᚦᛏ-7-ᚷ-ᛚᛄᛖᚫ`. This is the only Arabic numeral found in any unsolved rune page (aside from the base60/number grid pages). It may be:
- A page/section marker
- Part of the cipher key
- A transcription artifact

### 4.7 Section 0.6 (Partially Solved) as a Bridge

Section 0.6 (pages 20--24) is marked "partially solved" in solve_status. This is the immediate predecessor to the unsolved sections. Any partial decryption of 0.6 could reveal:
- The cipher transition point between solved and unsolved content
- Key derivation patterns (does each section derive its key from the previous section's plaintext?)
- Whether the F-skipping rule continues into LP2

The upstream docs show section 0.6 uses an unknown key. Page 21 has 58.2kB outguess garbage (same as the unsolved pages), linking it to the same steganographic system.

### 4.8 Recommended Attack Priority

Based on the analysis above, the recommended order for cryptanalysis attempts:

1. **Fix data integrity** for pages 71--72 (extract correct rune transcriptions from upstream liber_primus.md or rtkd/iddqd source).

2. **Section 0.7 (pages 25--31)** -- First unsolved section, follows partially solved 0.6. Highest frequency deviation suggests simplest cipher. The number grid on page 30 may contain key material.

3. **Section 0.9 (pages 40--43)** -- Shortest section (4 pages, 1,041 runes). If one cipher/key covers the whole section, the small corpus is easier to work with. Page 43's outguess data may provide a known-ciphertext anchor.

4. **Section 0.12 base60 grids (pages 64--66)** -- These are a completely different encoding from the rest of the LP. The 256 total values (byte range 0--255) suggest a lookup table or S-box. Solving these may unlock the cipher for adjacent rune pages.

5. **Section 0.12 rune pages (57--63, 67--70)** -- Largest contiguous rune block. Near-uniform frequency suggests a long key. May require the base60 grids as a decryption aid.

6. **Investigate the 58.2kB outguess data** -- Extract and compare the raw bytes from all eight pages. If they're identical, it's padding. If they differ but share structure, they may be a multi-part encrypted message.

---

## 5. Quick Reference: Outguess Status by Page

| Page | Section | Outguess Result |
|------|---------|----------------|
| 17 | 0.5 | 58.2kB garbage |
| 18 | 0.5 | none |
| 19 | 0.5 | none |
| 20 | 0.6 | none |
| 21 | 0.6 | 58.2kB garbage |
| 22 | 0.6 | none |
| 23--24 | 0.6 | (not documented) |
| 25--31 | 0.7 | (not documented) |
| 32--42 | 0.8--0.9 | (not documented) |
| 43 | 0.9 | 58.2kB garbage |
| 44--64 | 0.10--0.12 | (not documented) |
| 65 | 0.12 | 58.2kB garbage |
| 66 | 0.12 | none |
| 67 | 0.12 | none |
| 68 | 0.12 | 58.2kB garbage |
| 69 | 0.12 | 58.2kB garbage |
| 70 | 0.12 | 58.2kB garbage |
| 71 | 0.12 | 58.2kB garbage |
| 72 | 0.12 | none |

Pages marked "(not documented)" have no outguess analysis in the upstream liber_primus.md. Running outguess on all 75 JPGs to fill these gaps should be a priority.

---

## 6. Quick Reference: Global Rune Frequency (All Unsolved Pages)

| Rune | Unicode | Letter(s) | GP Value | Count | % of Total |
|------|---------|-----------|----------|-------|------------|
| ᚪ | U+16AA | A | 97 | 420 | 3.9% |
| ᛟ | U+16DF | OE | 83 | 407 | 3.8% |
| ᛁ | U+16C1 | I | 31 | 399 | 3.7% |
| ᚩ | U+16A9 | O | 7 | 394 | 3.7% |
| ᚢ | U+16A2 | U/V | 3 | 387 | 3.6% |
| ᛖ | U+16D6 | E | 67 | 387 | 3.6% |
| ᚠ | U+16A0 | F | 2 | 387 | 3.6% |
| ᛡ | U+16E1 | IA/IO | 107 | 384 | 3.6% |
| ᛒ | U+16D2 | B | 61 | 379 | 3.5% |
| ᚦ | U+16A6 | TH | 5 | 377 | 3.5% |
| ᛏ | U+16CF | T | 59 | 374 | 3.5% |
| ᚾ | U+16BE | N | 29 | 371 | 3.5% |
| ᚫ | U+16AB | AE | 101 | 370 | 3.4% |
| ᛄ | U+16C4 | J | 37 | 369 | 3.4% |
| ᛝ | U+16DD | NG/ING | 79 | 367 | 3.4% |
| ᛚ | U+16DA | L | 73 | 366 | 3.4% |
| ᛠ | U+16E0 | EA | 109 | 366 | 3.4% |
| ᛋ | U+16CB | S/Z | 53 | 365 | 3.4% |
| ᛞ | U+16DE | D | 89 | 363 | 3.4% |
| ᛗ | U+16D7 | M | 71 | 363 | 3.4% |
| ᛉ | U+16C9 | X | 47 | 362 | 3.4% |
| ᚣ | U+16A3 | Y | 103 | 361 | 3.4% |
| ᚱ | U+16B1 | R | 11 | 361 | 3.4% |
| ᚳ | U+16B3 | C/K | 13 | 359 | 3.3% |
| ᛈ | U+16C8 | P | 43 | 353 | 3.3% |
| ᚷ | U+16B7 | G | 17 | 352 | 3.3% |
| ᚹ | U+16B9 | W | 19 | 343 | 3.2% |
| ᚻ | U+16BB | H | 23 | 333 | 3.1% |
| ᛇ | U+16C7 | EO | 41 | 320 | 3.0% |

Expected uniform frequency: 3.45% (370.3 per rune). Range: 3.0%--3.9%. The distribution is remarkably flat, confirming strong polyalphabetic encryption.
