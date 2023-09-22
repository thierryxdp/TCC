def posLetra(f,l,n):
    i = 0
    retorno = 0 
    while i < len(f):
        if f[i] == l:
            retorno = retorno + 1
        if retorno == n:
            return i
        i = i + 1

    return -1