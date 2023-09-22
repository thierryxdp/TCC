def posLetra(texto,letra,ocorrencia):
    '''teste'''
    i=0
    x=0
    while i< len(texto):
        if texto[i]==letra:
            x=x+1
            if x== ocorrencia:
                return i
            
            i=i+1