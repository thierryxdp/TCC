def total(lista, dicionario):
    '''
    
    '''
    total = 0 
    for x in range(len(lista)):
        if lista[x] in dicionario:
            total += dicionario[lista[x]]
    return total