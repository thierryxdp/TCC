def posLetra(s,l,n):
    a = 0
    contador = 0
    f = list(s)
    while contador < (n-1):
        if l in f:
        	a = f.index(l)
        else:
            return -1
		del f[a]
    return a