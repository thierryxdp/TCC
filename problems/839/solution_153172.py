def carros(p, c=5):
    if p%c == 0:
        return p/c
    if p%c != 0:
        return (p//c) + 1