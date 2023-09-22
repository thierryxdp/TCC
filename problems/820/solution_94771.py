def posLetra(string,letra,ocorrencia):
    indice=0
    contador=0
    
    while contador<ocorrencia:
        if string[indice]==letra:
            contador=contador+1
            
            
        indice+=1
    return indice