from hashime.util import bit_set_in_pos, clamp, construct_matrix, matrix_to_art


def drunken_bishop(
    digest: bytes,
    width: int = 17,
    height: int = 9,
    chars: str = ' .o+=*BOX@%&#/^SE',
) -> str:
    x = start_x = width // 2
    y = start_y = height // 2
    # to index into the matrix use matrix[y][x]
    matrix = construct_matrix(width, height)

    for byte in digest:
        for i in range(0, 8, 2):
            # * 2 - 1 converts 0 and 1 into -1 and 1
            x_off = bit_set_in_pos(byte, i) * 2 - 1
            y_off = bit_set_in_pos(byte, i + 1) * 2 - 1
            # not going off the edge of the matrix
            x = clamp(x + x_off, 0, width - 1)
            y = clamp(y + y_off, 0, height - 1)
            matrix[y][x] = clamp(matrix[y][x] + 1, 0, len(chars) - 3)

    # overriding start and end characters
    matrix[start_y][start_x] = len(chars) - 2
    matrix[y][x] = len(chars) - 1

    return matrix_to_art(matrix, chars)
