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
