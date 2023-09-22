def total(lista,produtos):
    ''' '''
    i=0
    total=()
    for item in lista:
        if lista[i] in produtos:
            total+=lista[i]
    return round(total,2)