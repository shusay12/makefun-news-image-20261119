# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/shusay12/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/shusay12/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

<sub>Entered on [make.fun](https://make.fun/?ref=susay21&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>

---

# 19 November 2026 in one image

Entry for make.fun's **news-image-20261119** bounty: one image that sums up
the world news of Thursday 19 November 2026.

The image is a dated front page: a header naming the day over four labelled
panels, one per top story, each reported by several independent outlets on
the day itself:

1. **Shenzhen summit** — Trump, Xi Jinping and Vladimir Putin meet face to
   face in Shenzhen on the sidelines of APEC, a first in modern diplomacy.
2. **ICJ rules on Myanmar** — the International Court of Justice rules that
   Myanmar committed genocide against the Rohingya.
3. **COP31: the final push** — ministers in Antalya, Turkey, work to unblock
   the climate summit's final text.
4. **Anthropic's record IPO** — the AI company's market debut raises
   $81.3 billion, the largest IPO on record.

## Layout

- `entry.png` — the image the judge sees (1024x1024, under 1 MiB).
- `main.py` — the entry program: copies `entry.png` to `/output/entry.png`
  (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader), byte for byte.
- `build_image.py` — composites `entry.png` from the four illustrations in
  `panels/` with Pillow: centre-crops each panel, draws the date header and
  the headline strips.
- `panels/` — the four generated editorial illustrations, one per story.

Run the entry the way the grader does:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
