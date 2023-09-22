def posLetra(string,letra,n):
    indice = -1
    ocorrencia = 0
    while indice < len(string):
        if letra == string[indice]:
            indice +=1
            ocorrencia += 1
            return indice
        if contador == n:
            return indice
        if contador != n:
            return -1