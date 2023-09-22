def posLetra(f,l,n):
    if f.count(l) < n:
        return -1
    else:
        return f.count(l)