def precos (l,d):
    return map (ls, lambda s: d[s])
def total (l,d):
    return reduce (precos(l,d), lambda x,y: x+y,0)