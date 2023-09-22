def posLetra(x,l,n):
    r = x.find(l)
    while r >= 0 and n>1:
        r = x.find(l, r+1)
        n -= 1
    return r