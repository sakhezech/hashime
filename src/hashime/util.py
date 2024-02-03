def clamp(val: int, min_: int, max_: int) -> int:
    return min(max(val, min_), max_)


def bit_set_in_pos(num: int, pos: int) -> int:
    pow = 2**pos
    return (num & pow) // pow
