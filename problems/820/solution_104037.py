def posLetra(frase,letra,ocorrencia):
    lista = list(frase)
    i = 0
    c = 0
    while i in range(len(lista)):
        if lista[i] == letra:
            c = c + 1
            if c == ocorrencia:
                return i
        i = i + 1
    return -1