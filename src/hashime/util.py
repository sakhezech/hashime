import hashlib
from os import PathLike

StrPath = PathLike[str] | str


def clamp(val: int, min_: int, max_: int) -> int:
    """
    Clamps an int between two others.

    Args:
        val: Value to clamp.
        min_: Lower bound.
        max_: Upper bound.

    Returns:
        Clamped value.
    """
    return min(max(val, min_), max_)


def bit_set_in_pos(num: int, pos: int) -> int:
    """
    Gets a bit in position.

    Example::

        bin(4) == '0b100'
        bit_set_in_pos(4, 0) == 0
        bit_set_in_pos(4, 1) == 0
        bit_set_in_pos(4, 2) == 1

    Args:
        num: Value.
        pos: Position.

    Returns:
        Bit in position.
    """
    return (num >> pos) & 1


def bits_set_in_range(num: int, start: int, end: int) -> int:
    """
    Gets bits in range.

    Example::

        bin(52) == '0b110100'
        bin(5) == '0b101'
        bits_set_in_range(52, 2, 5) == 5

    Args:
        num: Value.
        start: Range start.
        end: Range end.

    Returns:
        Bits in range.
    """
    mask = (2 ** (end - start)) - 1
    return (num >> start) & mask


def file_digest(fp: StrPath, hash_function: str = 'sha256') -> bytes:
    """
    Gets a hash digest of a file.

    Args:
        fp: File path.
        hash_function: Hash function.

    Returns:
        File hash digest.
    """
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
    """
    Frames randomart.

    Args:
        art: Randomart to frame.
        top_text: Text on the top line.
        bottom_text: Text on the bottom line.
        brackets: Symbols surrounding text.
        lines: Frame side symbols in a clockwise order from the top.
        corners: Frame corner symbols in a clockwise order from the top-left.

    Returns:
        Framed randomart.
    """
    art_lines = art.split('\n')
    width = len(art_lines[0])

    # unpacking the values from tuples
    frame_t, frame_r, frame_b, frame_l = lines
    corner_tl, corner_tr, corner_br, corner_bl = corners

    br_len = len(brackets[0]) + len(brackets[1])
    if top_text is None:
        top_text = ''
    else:
        top_len = len(top_text) + br_len
        if top_len > width:
            top_text = top_text[: width - top_len - 3] + '...'
        top_text = top_text.join(brackets)

    if bottom_text is None:
        bottom_text = ''
    else:
        bot_len = len(bottom_text) + br_len
        if bot_len > width:
            bottom_text = bottom_text[: width - bot_len - 3] + '...'
        bottom_text = bottom_text.join(brackets)

    top_line = top_text.center(width, frame_t).join((corner_tl, corner_tr))
    bot_line = bottom_text.center(width, frame_b).join((corner_bl, corner_br))
    content = '\n'.join(f'{frame_l}{line}{frame_r}' for line in art_lines)
    return '\n'.join((top_line, content, bot_line))
