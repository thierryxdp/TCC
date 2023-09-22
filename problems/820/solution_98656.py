def posLetra(f, l, o):
    i = 0
    ocorrencia = 0
    while i < len(f):
        if f[i] == l:
            ocorrencia += 1
        if ocorrencia == o:
            return i
        i += 1
    return -1