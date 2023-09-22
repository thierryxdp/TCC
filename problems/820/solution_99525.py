def posLetra(frase,letra,ocorrencia):
    
    x = letra
    i=0
    posicao = -1
    
    while i<=ocorrencia:
        if letra in frase:
            posicao = frase.index(x,posicao+1)
        else:
            return -1
        i=i+1
    return posicao