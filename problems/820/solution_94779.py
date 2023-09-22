def posLetra(string,letra,ocorrencia):
    indice=0
    contador=0
    
    while indice<len(string):
        if string[indice]==letra:
            contador=contador+1
        if contador==ocorrencia:
            return indice
        indice+=1
    return -1