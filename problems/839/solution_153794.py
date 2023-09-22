def carros (x, *args):
    if not args:
        n = x//5
        return n
    else:
        y1 = args[0]
        y = int(y1)
        n = x//y
        return n