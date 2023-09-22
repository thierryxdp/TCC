def posLetra(frase,letra,ocorrencia):
    
    i=0
    posicao = -1
    rep = ocorrencia
    
    while i<=ocorrencia:
        if letra in frase:
            posicao = frase.index(letra,posicao+1)
            rep = rep -1 
        else:
            return -1
        i=i+1
    if rep == 0:
        return posicao
    else:
        return -1