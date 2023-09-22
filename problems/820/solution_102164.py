def posLetra(string, letra, ocorrencia):
    i = 0
    l = 0

    for letraselcionada in string:
        if i == ocorrencia:
            return l

        if letra == string[l]:
            i = i + 1
            l = l + 1
        elif letra != string[l]:
            l = l + 1
        else:
            return -1

    return l