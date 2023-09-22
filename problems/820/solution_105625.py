def posLetra(string,letra,n):
    indice = 0
    ocorrencia = 0
    while indice < len(string):
        if letra == string[indice]:
            ocorrencia += 1
        if ocorrencia == n:
            return indice
        if ocorrencia != n:
            indice += 1
        else:
            return -1