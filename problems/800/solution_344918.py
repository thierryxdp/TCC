def mapeia(ls,f):
    r = []
    for e in ls:
        r.append(f(e))
    return r

def precos(ls, d):
    return mapeia(ls, lambda s: d[s])

def lc(ls,d):
    return sum(precos(ls,d))