def posLetra(string,letra,ocorrencia):
    i = 0
    vezes = 0
    while i < len(string):
        if string[i] == letra:
            vezes = vezes + 1
            if vezes == ocorrencia:
                return i
        i = i + 1