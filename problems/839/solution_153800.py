import math

def carros (x, *args):
    if not args:
        n = math.ceil (x/5)
        return n
    else:
        y1 = args[0]
        y = int(y1)
        n = math.ceil(x/y)
        return n