def carros (x, *args):
    if not args[0]:
        n = x//5
        return n
    else:
        y1 = args[0]
        y = int(y)
        n = x//y
        return n