def posLetra(string,letra,n):
    indice = 0
    ocorrencia = 0
    while indice < len(string):
        if letra == string[indice] and ocorrencia == n:
            indice +=1
            ocorrencia += 1
            return indice
        if ocorrencia == n:
            return indice
        if ocorrencia != n:
            return -1