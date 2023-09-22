def mapeia (x,f):
    r = []
    for i in x:
        r.append(f(i))
    return r
def primo (n):
    ls = range (1, n+1)
    ds = mapeia (ls, lambda x:n%x ==0)
    return len (ls) == 2
def primo2 (n):
    if n == primo:
        return True
    else:
        return False