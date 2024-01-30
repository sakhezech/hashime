from typing import TypeVar

T = TypeVar('T')

Row = list
Matrix = list[Row[T]]


def clamp(val: int, min_: int, max_: int) -> int:
    return min(max(val, min_), max_)


def bit_set_in_pos(num: int, pos: int) -> int:
    pow = 2**pos
    return (num & pow) // pow


def construct_matrix(width: int, height: int, fill: T = 0) -> Matrix[T]:
    return [[fill for _ in range(width)] for _ in range(height)]


def matrix_to_art(matrix: Matrix[int], chars: str) -> str:
    return '\n'.join(
        ''.join(chars[clamp(val, 0, len(chars) - 1)] for val in row)
        for row in matrix
    )
