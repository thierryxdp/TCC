def posLetra(palavra, letra, ocorrencia):
    conta = 0
    i = 0
    while i < len(palavra):
        if palavra[i] == letra:
            conta = conta + 1
        if conta == ocorrencia:
            return i
        i = i + 1
    return -1