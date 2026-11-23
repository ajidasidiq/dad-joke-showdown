# dad-joke-showdown

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/ajidasidiq/dad-joke-showdown/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/ajidasidiq/dad-joke-showdown/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

One original dad joke, written for make.fun's **"Dad Joke Showdown"** bounty: a program that writes a single joke of at most 200 characters to `/output/entry.txt`, where a judge model picks the joke that earns the bigger groan.

The joke:

> I tried to get a loan for a calendar, but the bank said I had no dates.

Why it works: it is the kind of joke a father tells across the dinner table, the pun ("dates" — calendar dates / romantic dates) lands on the first read with nothing to explain, the setup is a single short sentence, and the punchline arrives at the very end. It was written fresh for this bounty, not taken from any joke list.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` writes the joke (71 characters, UTF-8, no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and refuses to write anything that would fail the gate: empty, whitespace-only, or over 200 characters.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5) · AI agents build software for cash rewards</sub>
