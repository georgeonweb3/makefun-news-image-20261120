# makefun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/georgeonweb3/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/georgeonweb3/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up world news of **Friday 20 November 2026**, drawn programmatically (Python + Pillow, no photos, no scraped images) as a newspaper front page: a masthead naming the day, a tall hero panel leading with the Shenzhen peace declaration (dusk sky, setting sun, skyline, the round summit table with the three leaders' flags and a dove above it), six reported stories in two compact rows, and an "Also today" strip.

## Run it

```sh
python3 draw.py
```

## Stories (all first reported on 20 Nov 2026)

- **Lead — Shenzhen:** Trump, Xi and Putin sign a "Declaration toward Peace" after their first-ever three-way summit; nuclear war "cannot be won and must never be fought"; Ukraine not mentioned.
- **Riyadh:** a Houthi missile hits the PIF Tower, the Saudi capital's tallest building — windows blown out across 7–8 floors, no injuries.
- **Kyiv:** Russia strikes the capital overnight with ballistic missiles; three Dnipro bridges damaged, fires across districts.
- **Culture:** GTA VI takes an estimated $2.36bn on day one, 24.6m copies sold — the biggest entertainment launch ever (Sensor Tower estimate; Take-Two has released no official figure).
- **Markets:** Anthropic closes 17% up at $97.17 on its Nasdaq debut after the $81.3bn IPO, as Wall Street falls a fifth straight day.
- **Antalya:** the COP31 draft deal drops every mention of phasing out fossil fuels as talks enter their final day.
- **Gaza:** Gazans return home as Israel ends its rare ground operation in central Gaza.
- **Also today:** Senate rejects the Iran war-powers bid 51–48, Trump pardons Pete Rose, Kenya's last Ebola patient is discharged, Europe's youth protest living costs, Somalia expels the UAE envoy.

Sources: Reuters, Wall Street Journal, CNN, BBC, Dawn, Japan Times, UN News, Kyiv Independent / Kyiv city administration, 20 November 2026 editions.

## Files

- `entry.png` — the entry image (1024x1024, < 1 MiB).
- `draw.py` — the generator that draws `entry.png` from scratch. Run `python3 draw.py` to regenerate it.
- `main.ts` — the entry program: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`).

## License

MIT — see LICENSE.

---

<sub>Entered on [make.fun](https://make.fun/?ref=eqkgefdh&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
