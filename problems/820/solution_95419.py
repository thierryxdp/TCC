def posLetra(string,letra,ocorrencia):
    contagem=str.count(string,letra)
    indice=0
    ocorrenciaDaVez = 0
    while ocorrenciaDaVez<ocorrencia:
        if string[indice]==letra:
            ocorrenciaDaVez+= 1
        indice+=1
        if contagem<ocorrencia:
            return -1
    return indice-1