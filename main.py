#!/usr/bin/env python3
"""Famous last words of a phone at 1 percent battery.

The joke is a confession with a twist: the phone was never really
dying. It has been sitting at 1 percent since Tuesday, faking its own
death, purely because it enjoys watching its owner panic every time
the low-battery warning blinks. The phone is the prankster, the owner
is the punchline, and the "last words" are not a farewell at all —
they are the reveal of a four-day con.

That is why it is the whole entry: one line, 105 characters, written
to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "Plot twist: I've been at 1 percent since Tuesday. "
    "I just enjoyed watching you panic every time I blinked."
)

assert 1 <= len(LINE) <= 199, "a last-words line must fit in 199 characters"


def main() -> None:
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
