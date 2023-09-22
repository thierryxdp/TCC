def posLetra(f,l,n):
    if n > str.count(f,l):
        return -1
    elif l == f[0]:
        return 0
    else:
        return str.index(f,l,n)
posLetra('eu te amo','e',1)