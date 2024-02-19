from hashime.matrix import Matrix
from hashime.util import bit_set_in_pos, bits_set_in_range

_fish_list = [
    Matrix.from_matrix([['>', '<', '>']]),
    Matrix.from_matrix([['<', '>', '<']]),
]


def fish_tank(
    digest: bytes,
    width: int = 17,
    height: int = 9,
    fish_list: list[Matrix[str]] = _fish_list,
) -> str:
    matrix = Matrix(width, height, fill=' ')

    for byte in digest:
        fish_type = bit_set_in_pos(byte, 0)
        x = bits_set_in_range(byte, 1, 5)
        y = bits_set_in_range(byte, 5, 8)
        x = int((x / 15) * width)
        y = int((y / 7) * height)
        fish = fish_list[fish_type]
        matrix.overlay(fish, x, y)

    return matrix.to_art(lambda x: x)
