def posLetra(frase,letra,ocorrencia):
    
    i=-1
    pos=-1
    
    while i<ocorrencia-1:
        if letra in frase:
            pos = frase.index(letra, pos+1)
        else:
            return -1
        i=i+1
    return pos