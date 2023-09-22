def total(lista, dicio):
    '''
    list, dict -> float
    '''
    total = 0
    for i in range(len(lista)):
        if lista[i] in dicio:
            total = total + dicio[i]
    return total