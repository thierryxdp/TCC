def total(lista,produtos):
    ''' '''
    i=0
    total=0
    for item in lista:
        if lista[i] in produtos:
            total+=produtos[lista[i]]
            i+=1
    return round(total,2)