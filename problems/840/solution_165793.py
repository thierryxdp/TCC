from math import floor
def bolos(a: int, b: int, c: int) -> int:
    return min(floor(a/2), floor(b/3), floor(c/5))