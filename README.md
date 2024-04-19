# hashime

[![CI](https://github.com/sakhezech/hashime/actions/workflows/ci.yaml/badge.svg)](https://github.com/sakhezech/hashime/actions/workflows/ci.yaml)

Hash visualization tool inspired by beautiful ssh-keygen randomart.

How can something so soulless be so pretty?

## Installation

From git:

```sh
pip install git+https://github.com/sakhezech/hashime
```

## Usage as CLI

`hashime ...` or `python -m hashime ...`

```console
$ hashime -h
usage: hashime [-h] [-v] [-l] [-lh] [-a ALGO] [-hf HASH] [--width WIDTH]
               [--height HEIGHT] [--no-frame] [--frame-top-text TOP_TEXT]
               [--frame-bottom-text BOTTOM_TEXT] [--frame-lines LINES]
               [--frame-corners CORNERS] [--frame-brackets BRACKETS]
               [--show-digest] [-f FILE] [-o OUT]

hash visualization tool

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -l, -la, --list-algo  show visualization algorithms and exit
  -lh, --list-hash      show available hashing functions and exit
  -a ALGO, --algorithm ALGO
                        visualization algorithm (defaults to DrunkenBishop)
  -hf HASH, --hash-function HASH
                        hashing function (defaults to sha256)
  --width WIDTH         visualization width
  --height HEIGHT       visualization height
  --no-frame            output visualization without a frame
  --frame-top-text TOP_TEXT
                        text on the top frame line
  --frame-bottom-text BOTTOM_TEXT
                        text on the bottom frame line
  --frame-lines LINES   comma-separated frame side symbols in a clockwise order
                        from the top
  --frame-corners CORNERS
                        comma-separated frame corner symbols in a clockwise
                        order from the top-left
  --frame-brackets BRACKETS
                        comma-separated symbols surrounding frame text
  --show-digest         output digest
  -f FILE, --file FILE  input file (defaults to stdin)
  -o OUT, --output OUT  output file (defaults to stdout)
```

## Usage in code

```py
>>> import hashime
>>> bishop = hashime.DrunkenBishop()
>>> bishop.update_fp('./LICENSE')
>>> art = bishop.to_art(
...     top_text='LICENSE',
...     bottom_text='SHA256',
...     brackets=('<', '>'),
...     lines=('═', '│', '─', '║'),
...     corners=('╔', '╕', '┘', '╙'),
... )
>>> print(art)
╔════<LICENSE>════╕
║    ..o +        │
║   o E.= o       │
║  o +.. o        │
║ . o o.o         │
║.   o =.S.       │
║..   o.+..+      │
║o.  o.oo+..=     │
║. . *+=..+o o .  │
║  .=+O.++  . o.. │
╙─────<SHA256>────┘
```

## Development

Use `ruff check --fix .` and `ruff format .` to check and format your code.

To get started:

```sh
git clone https://github.com/sakhezech/hashime
cd hashime
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```
