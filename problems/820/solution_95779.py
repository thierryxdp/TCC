def posLetra(strin,letra,ocorrencia):
    contador=0
    while contador<len(strin):
        letraOcorrencia=strin.find(letra,ocorrencia+contador)
        contador+=1
        if contador==ocorrencia:
                return letraOcorrencia
        else:
                return -1