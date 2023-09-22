def mapeia (x,f):
    r = []
    for i in x:
        r.append(f(i))
    return r
def primo (n):
    ls = range (1, n+1)
    ds = mapeia (ls, lambda x:n%x ==0)
    len (ls) == 2
        return ds (ls, lambda x:n%x ==0)