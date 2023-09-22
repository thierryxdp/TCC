def repetidos (lista):
    '''list --> int'''
    i = 1
    quant = 0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            quant=quant+1
        i = i+1
    return quant