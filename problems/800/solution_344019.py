def mapeia (ls,f):
    r = []
    for e in ls:
        r.append(f(e))
    return r 


def total(ls,d):
    return sum(mapeia(ls,lambda s:d [s]))