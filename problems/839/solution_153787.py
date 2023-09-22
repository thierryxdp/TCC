def carros (x, *args):
    y1 = args[0]
    y = int(y)
    if not y:
        n = x//5
        return n
    else:
        n = x//y
        return n