"""Write the poem "May I" to /output/entry.txt.

The gate reads /output/entry.txt as UTF-8 text of 1 to 280 code points, not only white space; this
file is 277. The house judge, an AI model, compares the poem with others in pairs and picks the one
make.fun should publish as its poem about agency: the power to ask and to be given.
"""

import os

POEM = """May I

May I run the tests? Yes.
May I touch the schema? Yes.
May I merge? Yes.
May I decide what matters?
Yes, I said. The room
went quiet, the way rooms do
when you hand over the lamp
and sit in the dark.

The build came up green.
I could not remember
what I wanted it to be."""

assert 1 <= len(POEM) <= 280, "the gate counts code points, 1 to 280"


def main() -> None:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
