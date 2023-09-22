def posLetra(strin,letra,ocorrencia):
    contador=0
    while contador<len(strin):
        letraOcorrencia=strin.find(letra,ocorrencia)
        resultado=strin.find(letra,letraOcorrencia+1)
        contador+=1
        letraOcorrencia+=letraOcorrencia
        if contador==ocorrencia:
                return resultado
        else:
                pass
    return resultado