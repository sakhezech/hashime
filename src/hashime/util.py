def clamp(val: int, min_: int, max_: int) -> int:
    return min(max(val, min_), max_)


def bit_set_in_pos(num: int, pos: int) -> int:
    pow = 2**pos
    return (num & pow) // pow


def frame(art: str) -> str:
    lines = art.split('\n')
    width = len(lines[0])
    horizontal_line = f'+{"-" * width}+'
    content = '\n'.join([f'|{line}|' for line in lines])
    return '\n'.join([horizontal_line, content, horizontal_line])
