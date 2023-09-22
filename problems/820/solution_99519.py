def posLetra(frase,letra,ocorrencia):
    
    i=0
    posicao = -1
    
    while i<=ocorrencia:
        if letra in frase:
            posicao = frase.index(letra,int(posicao)+1)
        else:
            return -1
        i=i+1
    return posicao