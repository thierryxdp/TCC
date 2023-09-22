import math
def bolos (a:int,b:int, c:int) -> int:
    return min(math.floor(a/2),math.floor(b/3),math.floor(c/5))