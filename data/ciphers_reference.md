# Ciphers & Techniques Reference

This is the comprehensive catalog of every cryptographic technique Cicada 3301 has used across the 2012, 2013, and 2014 puzzles, including the Liber Primus. For any future AI session attempting to determine what cipher an unsolved page might use, this is THE reference.

---

## Steganography

### OutGuess
- **What:** JPEG steganography tool that embeds data in the DCT coefficients of JPEG images.
- **Where used:** Nearly every JPEG image across all three years. This is Cicada's signature steganography method.
- **2012:** `1CcV1.jpg` (original /b/ image), `KXLOP.jpg` (Welcome subreddit image), `8D7hN.jpg` (Problems? subreddit image), `cicada.jpg` (845145127.com cicada image), QR code location images (`935691396441.jpg`, `876873892385.jpg`, `316744223127.jpg`, `162667212858.jpg`, etc.), `NHYLD.jpg` (Lady of Shallott, second chance)
- **2013:** `gqvvmk.jpg` (initial /b/ image), Gematria Primus image (XOR result of Twitter hex + 761.mp3)
- **2014:** `zN4h51m.jpg` (stage01 initial image), `1033.jpg` (first onion), `onion1.jpg`/`onion2.jpg`/`onion3.jpg` (stage03 three XOR images), server-status `05.jpg`, `03.jpg`/`04.jpg`, `06.jpg`-`09.jpg` (fourth onion gzip), `onion5portrait.jpg` (Goya painting), LP pages `00.jpg`-`16.jpg` (mixed: some yield PGP-signed messages, some yield hex data, some yield garbage)
- **How to extract:** `outguess -r image.jpg image.jpg.out`
- **Key detail:** The duck decoy image in 2012 hinted at OutGuess with the phrase "guess how to get the message out."
- **Repo artifacts:** `assets/2012/1CcV1.jpg.out`, `assets/2012/KXLOP.jpg.out`, `assets/2012/8D7hN.jpg.out`, `assets/2012/cicada.jpg.out`, `assets/2012/NHYLD.jpg.out`, `assets/2013/gematria-primus.jpg.out`, `assets/2014/stage01/` (zN4h51m.jpg)

### OpenPuff
- **What:** Multi-carrier steganography tool supporting multiple layers of obfuscation (cryptography, whitening, encoding).
- **Where used:** 2014 stage07 — `Interconnectedness.mp3` (the MP3 from the fifth onion)
- **Password:** `A = "33011033"`, `B` and `C` disabled. Use `mp3 > Maximum` setting. Requires OpenPuff v4.00 (newer versions incompatible).
- **What it yielded:** Three magic squares (5x5 summing to 3301, 7x7 summing to 1033, 5x5 summing to 1033).
- **Repo artifacts:** `assets/2014/stage07/index.mp3` (the Interconnectedness MP3), `assets/2014/stage07/magicsquares.txt` (output)

### ICMP Payload Encoding
- **What:** Data hidden in the payload of ICMP echo reply packets.
- **Where used:** 2013 — pinging the clearnet IP of `xsxnaksict6egxkq.onion` (`li498-122.members.linode.com`) returned duplicate ICMP echo replies with hex data in their payloads.
- **How it worked:** Each ping produced two responses: a normal one and an extra with sequence number 1 containing hex bytes. The hex data was interlaced across multiple pings and repeated. When concatenated, the hex formed a gzipped file (`message.txt.asc`) containing a PGP-signed message revealing the next onion address (`pklmx2eeh6fjt7zf.onion`).
- **Hint that led to it:** The Cicada message "knock on the sky and listen to the sound" pointed to pinging the server.

### Whitespace/Tab Binary Encoding
- **What:** Binary data encoded as spaces (0) and tabs (1) in HTML source code, then decoded to ASCII.
- **Where used:**
  - **2012:** `845145127.com` page source after Jan 11. The HTML `<pre>` block contained only tabs and spaces. Treating tab = 1 and space = 0, converting to binary, then ASCII yielded a PGP-signed message containing 10 twelve-digit numbers (image URLs for QR code locations).
  - **2013:** OutGuess of the Gematria Primus image contained a PGP-signed message whose body was only tabs and spaces. Decoded to binary then ASCII, it read: "Come to emiwp4muu2ktwknf.onion"
- **Repo artifacts:** `assets/2012/` (the 845145127.com source is described in `2012.md`)

### Trailing Spaces as Prime Sequences
- **What:** Extra spaces/plus signs appended to lines of PGP-signed messages, with counts forming prime number sequences.
- **Where used:**
  - **2013:** The `hello` response from the `emiwp4muu2ktwknf.onion` telnet shell. The PGP-signed message had empty lines with trailing spaces in the pattern 5-3-2-2-3-5.
  - **2014:** The `message.txt.asc` delivered to solver hidden services. Plus signs (`+`) were appended to lines, with counts forming the sequence: 2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37 (first 11 primes, OEIS A194954).

### Embedded Binary Data in Hex Dumps
- **What:** JPEG images (and other binary data) encoded as hexadecimal strings within HTML pages, often requiring XOR or bit-flipping to reveal.
- **Where used:** 2014 stages 03-06. Onion pages served long hex strings that, when converted to binary, contained JPEG images. Some required XOR with `0xFF` (bit-flipping). Third images were sometimes byte-reversed.
- **Specific instances:**
  - `cu343l33nqaekrnw.onion` (stage03): hex string XORed with 0xFF revealed three JPEGs; third was byte-reversed
  - `fv7lyucmeozzd5j4.onion` (stage04): Apache server-status page contained hex with two JPEGs and OOB data forming a magic square
  - `avowyfgl5lkzfj3n.onion` (stage05): hex yielding gzipped binary containing four JPEG images (06.jpg-09.jpg)
  - `ut3qtzbrvs7dtvzp.onion` (stage06): hex containing four sequential JPEGs (10.jpg-13.jpg)

### Bzip2-Compressed Steganography Output
- **What:** OutGuess output that is itself a bzip2-compressed file rather than plaintext.
- **Where used:** 2014 stage08 — OutGuess of `onion5portrait.jpg` (Portrait of Andres del Peral by Goya) yielded a bzip2-compressed file. Decompressing revealed a PGP-signed hex string containing 2 JPEGs and 1 MP3.

---

## Classical Ciphers

### Caesar Shift
- **What:** Simple letter substitution where each character is shifted by a fixed number.
- **Where used:** 2012 — The text appended to the original `1CcV1.jpg`: `TIBERIVS CLAVDIVS CAESAR says "lxxt>33m2mqkyv2gsq3q=w]O2ntk"`. Shifting by 4 to the right decoded to the URL `http://i.imgur.com/m9sYK.jpg`.
- **Parameters:** Shift = 4 (right/forward)
- **Repo artifacts:** `assets/2012/1CcV1.jpg` (tail of file contains the Caesar-encoded string)

### Vigenere Cipher (on Gematria Primus Alphabet)
- **What:** Polyalphabetic substitution cipher operating on the 29-rune Gematria Primus alphabet rather than the standard Latin alphabet. Each rune is shifted by the corresponding key rune's positional value.
- **Where used on solved LP pages:**
  - **LP pages 03-04:** Key = `DIVINITY` (GP values: 6, 19, 28, 19, 20, 19, 13, 3). Shift up forward Gematria. Every cleartext F appears as rune ᚠ (F) and must be skipped during decryption. Yields the "WELCOME" text.
  - **LP pages 14-15:** Key = `FIRFUMFERENFE` (GP values: 29, 19, 25, 29, 28, 10, 29, 11, 25, 11, 20, 29, 11). Shift up forward Gematria. Same F-skipping rule. Yields "A KOAN: THE I" text.
  - **LP pages 17-19:** Key = `FIRFUMFERENFE` (same as 14-15). Solved by the community. Section 0.5 of LP.
  - **2014 stage04 (LP pages 03-04 via server-status):** Key = `welcome pilgrim to the` (GP offsets: 22, 11, 9, 24, 26, 10, 11, 16, 19, 9, 23, 25, 19, 10, 13, 26, 27, 11). Yielded the onion address `avowyfgl5lkzfj3n.onion`.
- **Critical note:** The F-skipping rule means that any rune ᚠ in the ciphertext maps directly to cleartext F and does NOT consume a key position. This is unique to Cicada's Vigenere implementation.
- **Repo artifacts:** `assets/2014/liber-primus-complete/03.jpg` through `19.jpg`, `data/runes/` (rune transcriptions)

### Columnar Transposition
- **What:** Plaintext is written into rows of a fixed width, then columns are read out in a permuted order.
- **Where used:**
  - **2014 stage03** (`cu343l33nqaekrnw.onion`): XOR of three images yielded ciphertext arranged in 14 columns. Reordering columns by key `[2,8,9,1,12,13,11,4,5,7,3,0,6,10]` produced: "GOOD WORK ULTIMATE TRUTH IS THE ULTIMATE ILLUSION JOIN US AT FV7LYUCMEOZZD5J4ONION". Period = 14.
  - **2014 stage05** (OutGuess of LP page `08.jpg` from fourth onion gzip): Period = 7, key = `1736254`. Produced: "TO BELIEVE TRUTH IS TO DESTROY POSSIBILITY Q4UTGDI2N4M4UIM59133" (yielding `q4utgdi2n4m4uim59133.onion`).

### Book Codes
- **What:** Messages encoded as references to positions (line:character, paragraph:sentence:word:letter, chapter:line:character, etc.) in a specific book.
- **Where used:**
  - **2012 — The Mabinogion:** OutGuess of `1CcV1.jpg` contained a book code (line:character format). The "book" was text from The Mabinogion, decrypted via the subreddit key. Decoded to phone number `(214) 390-9608`. The subreddit usernames were anagrams: `CageThrottleUs` = Charlotte Guest, `ImagoOnNib` = Mabinogion.
  - **2012 — Agrippa by William Gibson:** "A poem of fading death, named for a king" pointed to Agrippa. Book code (line:character) decoded to the Tor address `sq6wmgv2zcsrix6t.onion`.
  - **2012 — Marriage of Heaven and Hell by William Blake:** Second-chance image `hkdgl.png` contained a book code referencing Blake's work. Decoded to onion address `cginiziglyaobyph.onion`.
  - **2013 — The Book of the Law (Liber AL vel Legis) by Aleister Crowley:** OutGuess of `gqvvmk.jpg` contained a book code in chapter:line:character format. Dashes were included as characters; spaces were not. Decoded to Dropbox URL `https://www.dropbox.com/s/r7sgeb5dtmzj14s/3301`.
  - **2014 — Self-Reliance by Ralph Waldo Emerson:** OutGuess of `zN4h51m.jpg` contained a book code in paragraph:sentence:word:letter format. The poem hint "The work of a private man who wished to transcend" pointed to Emerson. Decoded to `auqgnxjtvdbll3pv.onion`.
  - **2014 — Godel, Escher, Bach by Douglas Hofstadter:** The stage08 book code used chapter abbreviations (e.g., `3PI` = Three-Part Invention, `LML` = Little Harmonic Labyrinth) in chapter:line:word:letter format. The Godel+Escher+Bach connection was established via three binary files: a Godel incompleteness equation image, an Escher "Eye" painting, and a Bach Trio Sonata MP3. Decoded to `ut3qtzbrvs7dtvzp.onion`.
- **Repo artifacts:** `assets/2012/1CcV1.jpg.out` (Mabinogion book code), `assets/2012/hkdgl.png` (Blake), `assets/2013/gqvvmk.jpg` (Book of Law), `assets/2014/stage01/` (Self-Reliance)

### Subreddit Key / Polyalphabetic Shift
- **What:** A numeric key used to shift letters of scrambled text by varying amounts.
- **Where used:** 2012 — The subreddit `a2e7j6ic78h0j` had scrambled text posts. The full subreddit name `a2e7j6ic78h0j7eiejd0120` (hexadecimal) encoded the key `10, 2, 14, 7, 19, 6, 18, 12, 7, 8, 17, 0, 19, 7, 14, 18, 14, 19, 13, 0, 1, 2, 0`. Each letter of the scrambled text was shifted by the corresponding key number to produce the Mabinogion passage.

---

## Gematria Primus Substitution

The Gematria Primus (GP) is the fundamental encoding alphabet for the Liber Primus: 29 Anglo-Saxon runes, each mapped to a letter and a prime number (2-109). Authoritative mapping is in `data/gematria_primus.json`.

### Default (Direct Rune to Letter)
- **What:** Each rune maps directly to its assigned letter via the GP table.
- **Where used:** LP pages 00, 02, 05, 10, 11, 12, 13, 16, 74. The most common method for non-encrypted pages.
- **Note:** Some runes are ambiguous: ᚢ = U or V, ᚳ = C or K, ᛋ = S or Z. Some are digraphs: ᚦ = TH, ᛇ = EO, ᛝ = NG, ᛟ = OE, ᚫ = AE, ᛡ = IA/IO, ᛠ = EA.

### Reversed/Inverted Gematria
- **What:** The letter assignment order is reversed (the first rune maps to the last letter and vice versa). Specifically, GP 2013 rune values are used but then mapped through GP 2014 letter assignments, or vice versa.
- **Where used:** LP page 01 ("A WARNING"). Applying GP 2013 to the runes gives one set of letters; then applying GP 2014 mapping to those yields the plaintext.

### Shift N Down Reversed Gematria
- **What:** Reversed Gematria with an additional fixed shift of N positions.
- **Where used:** LP pages 06, 07, 08, 09. Shift = 3, direction = down, on reversed Gematria. Yields "A KOAN" and "AN INSTRUCTION" texts.

### Shift N Up Forward Gematria (Vigenere)
- **What:** Forward (default) Gematria with polyalphabetic shifts — this is the Vigenere cipher operating on the GP alphabet.
- **Where used:** See "Vigenere Cipher" section above. LP pages 03-04 (DIVINITY), 14-15 (FIRFUMFERENFE), 17-19 (FIRFUMFERENFE).

### phi(prime) Shift
- **What:** Euler's totient function applied to successive primes generates the keystream. Each rune is shifted down by phi(p_n) where p_n is the nth prime.
- **Where used:** LP page 73 ("AN END"). Shift down forward Gematria. The F-skipping rule applies. The page contains a deep web hash challenge.
- **Significance:** This is the most mathematically sophisticated key derivation used on any solved page. It suggests unsolved pages may use similarly derived keystreams from number-theoretic functions.

### Gematria Sums
- **What:** Not a cipher per se, but a validation technique. The GP prime values of all runes in a line/word are summed. On solved pages, these sums are consistently prime numbers, often emirps (primes that are also prime when reversed).
- **Where used:** LP pages 01 (line sums: 757, 1009, 691, 353, 769, 911, 1051, 859, 677), page 05 (line sums: 468, 853, 1039, 1237, 157). Also used in 2013 for the Parable verification: line sums 1259 * 1031 * 1229 = 1,595,277,641.
- **Repo artifacts:** `data/gematria_primus.json`

---

## Modern Cryptography

### RSA Encryption
- **What:** Asymmetric encryption using the RSA algorithm.
- **Where used:**
  - **2012:** Each solver who reached `sq6wmgv2zcsrix6t.onion` received a unique RSA-encrypted message with a deliberately weak modulus (breakable). Public exponent e = 65537. Individual n values were ~230 bits. Solvers had to factor n, decrypt, and submit the number back.
  - **2014 stage02** (`auqgnxjtvdbll3pv.onion`): OutGuess of `1033.jpg` contained an RSA-encrypted message (Crypt::RSA::ES::OAEP scheme, version 1.99). e = 65537, n was a breakable modulus. Decrypted to the next onion address `cu343l33nqaekrnw.onion`.
- **Implementation:** Perl module `Crypt::RSA` from CPAN.

### PGP Signing
- **What:** All official Cicada 3301 messages are cryptographically signed with GnuPG.
- **Key ID:** `7A35090F`
- **Full fingerprint:** `6D85 4CD7 9333 22A6 01C3 286D 181F 01E5 7A35 090F`
- **Key name:** "Cicada 3301 (845145127)"
- **Where used:** Every official message across all three years. Any unsigned message or message signed with a different key is NOT from Cicada.
- **Verification:** `gpg --verify message.asc`
- **Note:** The key is available on MIT keyservers. First announced in the OutGuess of the 2012 subreddit "Welcome" image.

### XOR Operations
- **What:** Bitwise exclusive-or of two or more data streams.
- **Where used:**
  - **2013:** Twitter hex data XORed with `761.mp3` produced the Gematria Primus JPEG image.
  - **2013:** Telnet `hint` output XORed with `560.00` from the CicadOS DATA folder produced the message "You can't see the forest when you're looking at the trees."
  - **2013:** Location phone call data XORed with `560.XX` files (where XX = dataset number) from DATA folder on the bootable ISO revealed onion addresses.
  - **2014 stage03:** Three JPEG images from `cu343l33nqaekrnw.onion` — OutGuess outputs XORed together (`onion1.bin XOR onion2.bin XOR onion3.bin`) yielded the PGP-signed columnar transposition ciphertext.
  - **2014 stage03 hex dump:** Bit-flipping (XOR with 0xFF) to reveal JPEG headers.
- **Repo artifacts:** `assets/2013/twitter.txt` (Twitter hex data), `assets/2013/cicados/AUDIO/761.MP3`, `assets/2013/cicados/DATA/`

### Shamir's Secret Sharing Scheme (SSSS)
- **What:** A threshold secret sharing scheme where a secret is split into n shares, any k of which can reconstruct it.
- **Where used:** 2013 — After calling phone numbers from physical poster locations and entering gematrified access codes, solvers received dataset/offset pairs. XORing with ISO data files revealed individual onion addresses. Each onion served an SSSS share. Once 5 of 10 shares were collected, they reconstructed the secret: `p7amjopgric7dfdi.onion`.
- **Threshold:** 5 of 10 shares needed.

---

## Encoding & Compression

### Base60
- **What:** Numbers represented in a base-60 system using a character set that maps to the Gematria Primus alphabet.
- **Where used:** LP pages 66, 67, 68 — These pages contain grids of base60-encoded numbers instead of runes. Page 66: 10x8 grid. Page 67: 13x8 grid (transcription marked "wrong!!!"). Page 68: 9x8 grid.
- **Status:** Unsolved. The base60 values may encode rune data in an alternate format.
- **Repo artifacts:** `assets/2014/liber-primus-complete/66.jpg`, `67.jpg`, `68.jpg`; transcriptions in `liber_primus.md` lines 1839-1940

### Hex Dumps
- **What:** Raw binary data represented as hexadecimal strings.
- **Where used:** Pervasive across all years — onion services frequently served hex-encoded binary data containing JPEG images, gzipped files, or PGP messages. The 2013 telnet `hello` response was entirely in hex. Multiple 2014 onion stages used hex as the primary data transport.
- **Decoding:** `xxd -r -p < hex_file > binary_file`

### Binary as Tabs/Spaces
- **What:** Binary encoding where tab = 1 and space = 0.
- **Where used:** See "Whitespace/Tab Binary Encoding" under Steganography.

### Gzip Compression
- **What:** Standard gzip compression (identified by `0x1F 0x8B` magic bytes).
- **Where used:**
  - **2013:** ICMP payload hex data was a gzipped `message.txt.asc`.
  - **2014 stage05** (`avowyfgl5lkzfj3n.onion`): PGP-signed hex was a gzip file containing four JPEG images (LP pages 06-09).
  - **2014 stage06** (`q4utgdi2n4m4uim5.onion`): Hex data was an MP3 file (Interconnectedness).

### Bzip2 Compression
- **What:** Bzip2 compression.
- **Where used:** 2014 stage08 — OutGuess of the Goya portrait yielded bzip2-compressed data. Decompressing gave a PGP-signed hex string containing images and audio.

---

## Audio & MIDI Encoding

### MIDI Note-to-Letter Substitution
- **What:** Musical notes encode letters based on their MIDI note number and duration.
- **Where used:** 2012 — After solving the RSA puzzle, solvers received a PGP-encrypted MIDI file. The MIDI contained two tracks. Track 2 was the encrypted message; Track 3 encoded the chorus of Blake's "A Song of Liberty" as a known-plaintext reference to derive the substitution key.
- **Key mapping:** Duration + note number = letter. For example: duration 24, note 55 = 'a'; duration 96, note 65 = 'o'; duration 192, note 60 = 't'; duration 384, note 55 = 'y'. Full key table in `2012.md`.
- **The encrypted message decoded to:** "very good you have proven to be most dedicated... create a gpg key... encrypt the following word list using the cicada 3301 public key..."

### Audio File Metadata & Hex Embedding
- **What:** Hidden messages embedded in audio file hex data and ID3 tags.
- **Where used:**
  - **2013:** `761.mp3` ("The Instar Emergence" by 3301). A hex dump revealed the Parable text: "Like the instar, tunneling to the surface / We must shed our own circumferences; / Find the divinity within and emerge." GP sums of each line multiply to the Parable number 1,595,277,641. The file length (167 seconds) and filename (761) are both primes; 167 reversed = 761.
  - **2014:** `Interconnectedness.mp3` from the fifth onion. GP sum of 'Interconnectedness' = 772. Song length = 277.133 seconds. Contained OpenPuff steganography.
- **Repo artifacts:** `assets/2013/cicados/AUDIO/761.MP3`, `assets/2014/stage07/index.mp3`

---

## Physical World Techniques

### QR Codes at GPS Coordinates
- **What:** Physical posters with cicada images and QR codes placed at specific GPS locations worldwide.
- **Where used:**
  - **2012:** 14 coordinates posted on `845145127.com`. Physical posters found at locations in Warsaw, Paris, Seattle, Arkansas, Miami, Hawaii, Sydney, etc. QR codes linked to unique image URLs on `845145127.com`; images contained OutGuess messages with book codes.
  - **2013:** Physical posters at multiple locations (Dallas TX, Okinawa Japan, Moscow Russia, Little Rock AR, Annapolis MD, Portland OR, Columbus GA) with phone numbers ending in 3301 or 1033, plus access codes.

### Phone Numbers with Recorded Messages
- **What:** Telephone numbers that play recorded clues when called.
- **Where used:**
  - **2012:** `(214) 390-9608` — recording mentioned three prime numbers associated with the original image (509, 503, 3301; product = 845145127).
  - **2013:** Phone numbers on physical posters. Callers entered gematrified access codes to receive dataset/offset pairs for XOR decryption.

---

## Mathematical Constructs

### Magic Squares
- **What:** n x n grids of numbers where all rows, columns, and diagonals sum to the same "magic constant."
- **Where used:**
  - **LP page 05:** 5x5 magic square with magic constant 1033. Words in the grid (SHADOWS, AETHEREAL, BUFFERS, VOID, CARNAL, OBSCURA, FORM, MOBIUS, ANALOG, MOURNFUL, CABAL) translate to GP values.
  - **2014 stage04:** 5x5 magic square (sum 1033) found in OOB data between two JPEGs.
  - **2014 stage07:** Three magic squares from OpenPuff extraction: 5x5 (sum 3301), 7x7 (sum 1033), 5x5 (sum 1033).
  - **2014 stage06:** Solvers had to submit valid magic squares to proceed.

### Prime Number Sequences
- **What:** Primes and prime-related sequences used as structural elements throughout.
- **Key instances:**
  - Image dimensions: 509x503 pixels (both prime)
  - Product: 509 * 503 * 3301 = 845145127
  - CicadOS boot sequence: prints all primes up to 3301, pausing at 1033 and 3301
  - Trailing spaces encoding prime sequences (2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37)
  - GP values are the first 29 primes (2-109)
  - Line sums on solved LP pages are consistently prime
  - Gematria sum of "Patience is a virtue" = 761 (palindromic prime)
  - File lengths and names often prime (761.mp3 = 167 seconds; both prime)

### Totient Function (Euler's phi)
- **What:** phi(n) = count of integers less than n that are coprime to n. For primes p, phi(p) = p-1.
- **Where used:** LP page 73 keystream. Referenced explicitly on LP page 05: "THE TOTIENT FUNCTION IS SACRED."

---

## Tor Hidden Services & Network Techniques

### Onion Address Derivation
- **What:** Each puzzle stage typically decrypts to a `.onion` address for the next stage.
- **Onion chain (2014):**
  1. `auqgnxjtvdbll3pv.onion` (from Self-Reliance book code)
  2. `cu343l33nqaekrnw.onion` (from RSA decryption)
  3. `fv7lyucmeozzd5j4.onion` (from columnar transposition)
  4. `avowyfgl5lkzfj3n.onion` (from Vigenere on LP 03-04 runes)
  5. `q4utgdi2n4m4uim59133.onion` (from columnar transposition of LP 08)
  6. `ut3qtzbrvs7dtvzp.onion` (from GEB book code)
  7. `ky2khlqdf7qdznac.onion` (delivered to solver hidden services, contained LP2)

### Growing Hex Strings
- **What:** Onion pages that slowly appended hex characters over time, at intervals that were multiples of 5 minutes.
- **Where used:** 2014 stages 03-05. The growing string on `cu343l33nqaekrnw.onion` grew for ~23 hours. The string on `fv7lyucmeozzd5j4.onion` grew similarly. Both had 512-character (256-byte) initial strings that matched between stages.

### Server Status Page Leaks
- **What:** Apache server-status pages that (possibly intentionally) leaked additional hex data.
- **Where used:** 2014 stage04 — A solver ran a scanner against `fv7lyucmeozzd5j4.onion` and found an Apache server-status page containing a long hex string with embedded JPEG images and OOB data.

---

## Summary: Unsolved LP Pages & Candidate Ciphers

Based on the patterns above, the 56 unsolved LP pages (17-72, noting 17-19 are solved with FIRFUMFERENFE) likely use some combination of:

1. **Vigenere on GP alphabet** — The most common encryption method for multi-page sections. Keys may derive from:
   - Words in the solved philosophical text
   - GP sums or other mathematical derivations
   - The 2016 hint: "its words are the map, their meaning is the road, their numbers are the direction"

2. **Shifted Gematria** — Fixed-shift variants (like the shift-3 on pages 06-09) with unknown shift values.

3. **Totient/prime-based keystreams** — Like page 73's phi(prime) key, other number-theoretic functions could generate keystreams.

4. **Unknown cipher types** — The community has attempted Hill cipher, Atbash, Autokey, Playfair, and brute-force Vigenere without success on the bulk of LP2.

5. **Base60 decoding** — Pages 66-68 require understanding the base60-to-rune mapping before any cipher analysis.

Key validation method: if a candidate decryption produces text whose GP line sums are consistently prime, it is almost certainly correct.

---

## Quick-Reference: Cipher Used Per Solved Page

| Pages | Cipher | Key | Direction |
|-------|--------|-----|-----------|
| 00, 02 | Cleartext | -- | -- |
| 01 | Reversed Gematria | -- | Inverted mapping |
| 03-04 | Vigenere | DIVINITY | Shift up forward GP |
| 05, 10-13, 16, 74 | Default GP substitution | -- | Direct mapping |
| 06-09 | Shifted reversed GP | 3 | Shift 3 down reversed |
| 14-15, 17-19 | Vigenere | FIRFUMFERENFE | Shift up forward GP |
| 73 | phi(prime) shift | Totient keystream | Shift down forward GP |
