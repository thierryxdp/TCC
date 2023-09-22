import math
def colchao([medidas],H,L):
    a = math.sqrt((H**2) + (L**2))
    if medidas[1] < H and medidas[2] < L:
        return True
    if medidas[1] < a:
        return True
    else:
        return False