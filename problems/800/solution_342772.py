def total(lista,produtos):
    ''' '''
    i=0
    total=()
    for item in lista:
        if lista[i] in produtos:
            total+=prdutos(lista[i])
        i+=1
    return round(total,2)