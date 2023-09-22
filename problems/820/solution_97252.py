def posLetra(numero)
    """ """
    i = 0
    ocorrencia = 0
    a = str.count(frase,letra)
    if a < numero:
        return -1
    while ocorrencia < numero:
        if frase[i] == letra:
            ocorrencia += 1
            i += 1
    return i-1