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
def total (l,d):
    f = round (precos(l,d),2.00)
    return reduz (f, lambda x,y: x+y,0)