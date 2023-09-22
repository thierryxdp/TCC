def carros (x, *args):
    y = int(args)
    if not y:
        n = x//5
        return n
    else:
        n = x//y
        return n