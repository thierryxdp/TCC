def posLetra(string, letra, n_ocorrencia):
    for index, letter in enumerate(string):
        if letter == letra:
            n_ocorrencia -=1
            if n_ocorrencia == 0:
                return index
    return -1