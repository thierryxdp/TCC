def precos(ls, d):
    return mapeia(ls, lambda s: d[s])

def total(ls, d):
    return reduz(precos(ls, d), lambda x, y: x + y, 0)