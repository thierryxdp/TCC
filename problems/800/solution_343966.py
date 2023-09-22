def precos(ls, d):
    return mapeia(ls, lambda s: d[s])

def total(ls, d):
    def precos(ls, d):
    return mapeia(ls, lambda s: d[s])
    return reduz(precos(ls, d), lambda x, y: x + y, 0)