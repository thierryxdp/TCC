def mapeia (ls, f):
    r = []
    for e in ls:
        if p(e):
            r.append(e)
    return r

def primo (n):
    ls = range (1, n+1)
    ds = mapeia(ls, lambda x: n%x==0)
    return len(ds)==2