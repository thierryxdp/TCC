def posLetra(string, letra, ocorrencia):
    indice = 0
    for i in range(len(string)):
        if string[i] == letra:
            indice += 1
        if indice == ocorrencia:
            return i
    return -1