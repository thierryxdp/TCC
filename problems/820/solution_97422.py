def posLetra(s,l,n):
    a = 0
    contador = 0
    f = list(s)
    while contador < n:
        if l in f:
        	a = f.index(l)
        else:
            return f
        del f[a]
    return