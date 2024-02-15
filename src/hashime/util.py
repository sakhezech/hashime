def clamp(val: int, min_: int, max_: int) -> int:
    return min(max(val, min_), max_)


def bit_set_in_pos(num: int, pos: int) -> int:
    return (num >> pos) & 1


def bits_set_in_range(num: int, start: int, end: int) -> int:
    mask = (2 ** (end - start)) - 1
    return (num >> start) & mask


def frame(art: str) -> str:
    lines = art.split('\n')
    width = len(lines[0])
    horizontal_line = f'+{"-" * width}+'
    content = '\n'.join([f'|{line}|' for line in lines])
    return '\n'.join([horizontal_line, content, horizontal_line])
