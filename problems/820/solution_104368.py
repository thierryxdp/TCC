def posLetra(f,l,n):
    i = 0
    resultado = 0
    pos = 1
    ocorrencias = f.count("l")
    while i < ocorrencias:
        if f[i] == l:
            resultado = resultado + i
        else:
            resultado = -1
        i = i + 1
        pos = pos + 1
    return pos