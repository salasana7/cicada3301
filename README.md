<p align="middle"><img src="assets/2012/cicada.jpg" alt="cicada.jpg" width="600" border="2"></p>

## About This Fork

This is a fork of [scream314/cicada3301](https://github.com/scream314/cicada3301), restructured for **AI-assisted cryptanalysis** of the Liber Primus.

Of the 75 runic pages in the Liber Primus, **56 remain unsolved** after 12+ years of community effort. This fork adds machine-readable data files so that LLMs like Claude can efficiently load the puzzle state and contribute to analysis. As of April 2026, no LLM has been systematically applied to the unsolved pages.

**See [CLAUDE.md](CLAUDE.md) for AI assistant onboarding instructions.**

## What's New in This Fork

| File | Description |
|------|-------------|
| [CLAUDE.md](CLAUDE.md) | AI onboarding: what to load first, how to approach analysis |
| [data/gematria_primus.json](data/gematria_primus.json) | The Rosetta Stone: 29 runes mapped to letters and prime values (JSON) |
| [data/solve_status.md](data/solve_status.md) | Which pages are solved/unsolved, what cipher, what key |
| [data/runes/](data/runes/) | 75 individual rune transcription files (one per LP page) |

Data sourced from [rtkd/iddqd](https://github.com/rtkd/iddqd), [Taiiwo/cicada](https://github.com/Taiiwo/cicada), [iBotPeaches/cicada_3301](https://github.com/iBotPeaches/cicada_3301), and the [CicadaSolvers](https://www.cicadasolvers.com) community.

---

## Original Content

Almost all original files are under [assets/](assets/) sorted by year.

The full Liber Primus is [here](assets/2014/liber-primus-complete).

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
  
### Links and Sources
Upstream credits: [useful links](links.md), [#cicadasolvers](http://webchat.freenode.net/?channels=cicadasolvers) (defunct?), [CicadaSolvers Discord](https://discord.com/channels/572330844056715284/).

Additional sources for this fork: [rtkd/iddqd](https://github.com/rtkd/iddqd) (master transcriptions), [cicada-solvers org](https://github.com/cicada-solvers) (53 repos of community tools), [Uncovering Cicada Wiki](https://uncovering-cicada.fandom.com/), [CicadaSolvers.com quickstart](https://www.cicadasolvers.com/quickstart/), [Connor Tumbleson's Puzzle 3 blog series](https://connortumbleson.com/2021/02/15/the-cicada-3301-mystery-puzzle-3-part1/).
