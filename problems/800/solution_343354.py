def total(lista,dicio):
    '''
    '''
    valor=0
    i=0
    
    while i<len(lista):
        if lista[i] in dict.keys(dicio):
            valor=valor+dict.get(dicio,lista[i])
        i=i+1
    return round(valor,2)