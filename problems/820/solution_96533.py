def posLetra(frase,letra,ocorrencia):
    
    i=1
    
    if ocorrencia>str.count(frase,letra):
        return -1
    else:
        while i<ocorrencia:
            frase=str.replace(frase,letra,'0',1)
            i=i+1
            
        return: str.index(frase,letra)