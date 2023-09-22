def total(lista=[],dict={}):
    cont = 0.0
    for i in lista:
        cont+=doct[i]
    return round(cont, 2)