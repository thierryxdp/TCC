def posLetra(frase, x, n):
    ocorrencia  = 0
    for i in range(len(frase)):
        h = frase[i]
        if i == x:
            ocorrencia  = ocorrencia  + 1
        if ocorrencia == n:
            return