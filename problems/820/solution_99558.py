def posLetra(frase,letra,ocorrencia):
    
    i=-1
    teste = 0
    
    while i!=ocorrencia:
        if letra in frase:
            teste = frase.index(letra, i)
        else:
            return -1
        i=i+1
    return teste