def posLetra(frase,letra,ocorrencia):
    
    i=0
    posicao = 0
    rep = ocorrencia
    
    if letra in frase:
        while rep>0:
            if letra == frase[i]:
            rep = rep - 1
            posicao = posicao + 1
        else: 
            posicao = posicao + 1
        i = i+1
    return posicao-1
    else:
        return -1