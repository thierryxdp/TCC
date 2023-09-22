def mapeia (l,d):
    r = []
    for x in l:
        r.append(d(x))
    return r
def reduz (l, d, init):
    r = init
    for x in l:
        r = d (r,x)
    return r
def precos (l,d):
    return mapeia (l, lambda s: d[s])
def lista (l,d):
    return reduz (precos(l,d), lambda x,y: x+y,0)
def total (l,d):
    return round(lista (l,d), 2)