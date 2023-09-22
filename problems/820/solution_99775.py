def posLetra(frase,letra,ocorrencia):
    
    i=0
    posicao = 0
    
    while i<=ocorrencia:
        if len(frase)<=i:
            posicao = frase.index(letra,i)
        else:
            return -1
        i = i+1
    return posicao