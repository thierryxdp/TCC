def total(lista, dicio):
    '''
    list, dict -> float
    '''
    total = 0
    for i in lista:
        if lista[i] in dicio:
            total = total + dicio[i]
    return total