def total(lista,produtos):
    aux=0
    for x in lista:
        aux+=produtos[x]
    return round(aux,2)