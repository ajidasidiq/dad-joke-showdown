"""Dad Joke Showdown entry.

Writes a single original dad joke to the output directory the grader
provides, as /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The joke (written fresh for this bounty):

    I tried to get a loan for a calendar, but the bank said I had no dates.

Why it works as a dad joke: a father could say it across the dinner
table, the pun ("dates" -- calendar dates / romantic dates) lands on the
first read with no explaining, the setup is one short sentence, and the
punchline arrives at the very end.
"""

import os

JOKE = "I tried to get a loan for a calendar, but the bank said I had no dates."


def main() -> None:
    # The sealed gate accepts only UTF-8 text of 1 to 200 characters that
    # is not only white space, so refuse to write anything outside it.
    if not JOKE.strip() or len(JOKE) > 200:
        raise SystemExit("entry joke fails the 1-200 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {entry_path}")


if __name__ == "__main__":
    main()
