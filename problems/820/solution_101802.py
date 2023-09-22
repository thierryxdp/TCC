def posLetra(s,l,i):
    p = s.find(l)
    while p >= 0 and i > 1:
        p = s.find(l,p+1)
        i = i-1
    return p