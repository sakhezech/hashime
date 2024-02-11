import argparse
import base64
import hashlib
import sys
from io import BufferedReader, TextIOWrapper
from typing import Any, Sequence

from hashime.__version__ import __version__
from hashime.drunken_bishop import drunken_bishop
from hashime.util import frame

_algorithms = [drunken_bishop]


def cli(argv: Sequence[str] | None = None):
    algorithms = {algorithm.__name__: algorithm for algorithm in _algorithms}
    parser = argparse.ArgumentParser(
        prog='hashime',
        description='hash visualization tool',
    )

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=__version__,
    )

    parser.add_argument(
        '-l',
        '-la',
        '--list-algo',
        action=PrintAndExitAction,
        const=', '.join(algorithms.keys()),
        help='show visualization algorithms and exit',
    )

    parser.add_argument(
        '-lh',
        '--list-hash',
        action=PrintAndExitAction,
        const=', '.join(hashlib.algorithms_available),
        help='show available hashing functions and exit',
    )

    parser.add_argument(
        '-a',
        '--algorithm',
        choices=algorithms.keys(),
        default='drunken_bishop',
        metavar='ALGO',
        help='visualization algorithm (defaults to drunken_bishop)',
    )

    parser.add_argument(
        '--hash-function',
        choices=hashlib.algorithms_available,
        default='sha256',
        metavar='HASH',
        help='hashing function (defaults to sha256)',
    )

    parser.add_argument(
        '--width',
        type=int,
        default=17,
        help='visualization width (defaults to 17)',
    )

    parser.add_argument(
        '--height',
        type=int,
        default=9,
        help='visualization height (defaults to 9)',
    )

    parser.add_argument(
        '--no-frame',
        action='store_true',
        help='output visualization without a frame',
    )

    parser.add_argument(
        '--show-digest',
        action='store_true',
        help='output digest',
    )

    parser.add_argument(
        '-f',
        '--file',
        type=argparse.FileType('br'),
        default='-',
        help='input file (defaults to stdin)',
    )

    parser.add_argument(
        '-o',
        '--output',
        type=argparse.FileType('w'),
        default='-',
        metavar='OUT',
        help='output file (defaults to stdout)',
    )

    args = parser.parse_args(argv)

    algorithm = algorithms[args.algorithm]
    hash_function: str = args.hash_function
    should_be_framed: bool = not args.no_frame
    should_show_digest: bool = args.show_digest
    out: TextIOWrapper = args.output
    file: BufferedReader = args.file

    kwargs: dict[str, Any] = {
        'width': args.width,
        'height': args.height,
    }

    digest = hashlib.file_digest(file, hash_function).digest()

    art = algorithm(digest, **kwargs)
    if should_be_framed:
        art = frame(art)

    out.write(art)
    out.write('\n')
    if should_show_digest:
        encoded = base64.standard_b64encode(digest).decode()
        out.write(f'{hash_function}: {encoded}\n')


class PrintAndExitAction(argparse.Action):
    def __init__(
        self,
        option_strings,
        const=None,
        dest=argparse.SUPPRESS,
        default=argparse.SUPPRESS,
        help=None,
    ):
        super(PrintAndExitAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            const=const,
            nargs=0,
            help=help,
        )
        self.text = const

    def __call__(self, parser, namespace, values, option_string=None):
        text = self.text
        if text is None:
            text = ''
        formatter = parser._get_formatter()
        formatter.add_text(text)
        parser._print_message(formatter.format_help(), sys.stdout)
        parser.exit()


if __name__ == '__main__':
    cli()
