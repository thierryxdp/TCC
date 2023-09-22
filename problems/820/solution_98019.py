def posLetra(f,l,q):
    x = 0
    i = 0
    while q != x:
        if f[i] == l:
            x += 1
        i += 1
    return i-1