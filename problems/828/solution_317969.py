def filtra (ls, p):
    r = []
    for e in ls:
        if p(e):
            r.append (e)
    return r

def mapeia (ls, f):
    r = []
    for e in ls:
        r.append(f(e))
    return r

def primo (n):
    ls = range (1, (n+1))
    ds = filtra (ls, lambda x: n%x==0)
    return len (ds) == 2