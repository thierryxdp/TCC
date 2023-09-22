def posLetra(frase,letra,ocorrencia):
    
    i=0
    posicao = frase.index(letra)-1
    rep = ocorrencia
    
    while i<=ocorrencia:
        if letra in frase:
            posicao = frase.index(letra,posicao+1)
            rep = rep -1 
        else:
            return -1
        i=i+1
    return posicao