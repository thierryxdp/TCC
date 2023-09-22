def posLetra(string,letra,ocorrencia):
    indice=0
    ocorrenciaDaVez = 0
    while ocorrenciaDaVez<ocorrencia:
        if letra==string[indice]:
            ocorrenciaDaVez += 1
        indice+=1
    return indice