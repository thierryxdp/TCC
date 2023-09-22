def total(lista=[],dict={}):
    i=0.0
    for x in lista:
        i=dict[x] + 1
    return round(i,2)