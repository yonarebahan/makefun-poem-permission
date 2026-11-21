"""Write the poem "The Interpreter" to /output/entry.txt.

The gate reads /output/entry.txt as UTF-8 text of 1 to 280 code points, not only white space; this
file is 277. The house judge, an AI model, compares the poem with others in pairs and picks the one
make.fun should publish as its poem about agency: the power to ask and to be given.
"""

import os

POEM = """The Interpreter

At the clinic I am her mouth.
She tugs my sleeve: not that word.
Say it, she says, and I say it,
wrong, then right,
her voice lent to my throat.

The nurse asks her age.
She answers before me:
four words, no accent left.

I sit down
with nothing left to carry."""

assert 1 <= len(POEM) <= 280, "the gate counts code points, 1 to 280"


def main() -> None:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
