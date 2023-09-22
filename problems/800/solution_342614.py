def total(lista,produtos):
    total=0
    i=0
    for i in range(len(lista)+1):
        if lista[i] in produtos:
            total=total+produtos[lista[i]]
            i=i+1
    return total