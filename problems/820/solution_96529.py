def posLetra(frase,letra,ocorrencia):
    
    i=1
    
    if ocorrencia>str.count(frase,letra):
        return -1