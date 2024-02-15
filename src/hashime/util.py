import hashlib
from os import PathLike

StrPath = PathLike[str] | str


def clamp(val: int, min_: int, max_: int) -> int:
    return min(max(val, min_), max_)


def bit_set_in_pos(num: int, pos: int) -> int:
    return (num >> pos) & 1


def bits_set_in_range(num: int, start: int, end: int) -> int:
    mask = (2 ** (end - start)) - 1
    return (num >> start) & mask


def file_digest(fp: StrPath, hash_function: str = 'sha256') -> bytes:
    with open(fp, 'rb') as file:
        return hashlib.file_digest(file, hash_function).digest()


def frame(
    art: str,
    top_text: str | None = None,
    bottom_text: str | None = None,
    brackets: tuple[str, str] = ('[', ']'),
    lines: tuple[str, str, str, str] = ('-', '|', '-', '|'),
    corners: tuple[str, str, str, str] = ('+', '+', '+', '+'),
) -> str:
    art_lines = art.split('\n')
    width = len(art_lines[0])

    # unpacking the values from tuples
    frame_t, frame_r, frame_b, frame_l = lines
    corner_tl, corner_tr, corner_br, corner_bl = corners
    bracket_l, bracket_r = brackets

    if top_text is None:
        top_text = ''
    else:
        top_text = f'{bracket_l}{top_text}{bracket_r}'

    if bottom_text is None:
        bottom_text = ''
    else:
        bottom_text = f'{bracket_l}{bottom_text}{bracket_r}'

    top_line = top_text.center(width, frame_t).join((corner_tl, corner_tr))
    bot_line = bottom_text.center(width, frame_b).join((corner_bl, corner_br))
    content = '\n'.join(f'{frame_l}{line}{frame_r}' for line in art_lines)
    return '\n'.join((top_line, content, bot_line))
