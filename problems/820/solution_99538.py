def posLetra(frase,letra,ocorrencia):
    
    i=0
    posicao = 0
    teste = 0
    
    while i<=ocorrencia:
        if letra in frase:
            teste = frase.index(letra, posicao )
        else:
            return -1
        posicao = posicao + 1
        i=i+1
    return teste