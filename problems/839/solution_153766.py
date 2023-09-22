def carros (*args):
    x = args[1]
    y = args[2]
    if not y:
        n = x//5
        return n
    else:
        n = x//y
        return n