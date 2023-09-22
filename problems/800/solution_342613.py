def total(lista,produtos):
    total=0
    for i in range(0,len(lista)+1):
        if lista[i] in produtos:
            total=total+produtos[lista[i]]
    return total