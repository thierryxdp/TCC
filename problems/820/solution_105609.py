def posLetra(s, l, n):
    x=s.find(l)
    while x>=0 and n>1:
        x=s.find(l, x+1)
        n-=1
    return x