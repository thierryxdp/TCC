def total(lista, dicio):
    '''
    '''
    
    i=0
    final=0
    compra=lista[i]
    
    for produtos in lista:
        if lista[i] in dicio:
            final+=dicio[compra]
    
    return round(final,2)