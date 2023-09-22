def posLetra(f,l,n):
    i = 0
    resultado = 0
    while i < len(f):
        if f[i] == l:
            resultado = f[i].index
        i = i + 1
    return resultado