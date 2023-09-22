def posLetra(f,l,n):
    i = 0
    resultado = 0
    pos = 1
    while i < len(f):
        if f[i] == l:
            resultado = resultado + i
        else:
            resultado = -1
        i = i + 1
        pos = pos + 1
    return pos