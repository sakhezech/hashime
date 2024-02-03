from hashime.matrix import Matrix
from hashime.util import bit_set_in_pos, clamp


def drunken_bishop(
    digest: bytes,
    width: int = 17,
    height: int = 9,
    chars: str = ' .o+=*BOX@%&#/^SE',
) -> str:
    x = start_x = width // 2
    y = start_y = height // 2
    matrix = Matrix(width, height, fill=0)

    for byte in digest:
        for i in range(0, 8, 2):
            # * 2 - 1 converts 0 and 1 into -1 and 1
            x_off = bit_set_in_pos(byte, i) * 2 - 1
            y_off = bit_set_in_pos(byte, i + 1) * 2 - 1
            # not going off the edge of the matrix
            x = clamp(x + x_off, 0, width - 1)
            y = clamp(y + y_off, 0, height - 1)
            matrix[x, y] = clamp(matrix[x, y] + 1, 0, len(chars) - 3)

    # overriding start and end characters
    matrix[start_x, start_y] = len(chars) - 2
    matrix[x, y] = len(chars) - 1

    return matrix.to_art(lambda x: chars[clamp(x, 0, len(chars) - 1)])
