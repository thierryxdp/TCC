def total(lista, dicio):
    '''
    list, dict -> float
    '''
    total = 0
    for i in dicio:
        if lista[i] in d:
            total = total + dicio[i]
    return total