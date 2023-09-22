def posLetra(frase, x, n):
    ocorrencia  = 0
    for i in range(len(frase)):
        h = frase[i]
        if h == x:
            ocorrencia  = ocorrencia  + 1
        if ocorrencia == n:
            return i