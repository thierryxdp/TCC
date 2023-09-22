def total(lista,produtos):
    v=0
    for p in lista:
        if p in produtos:
            v+=dict.get(produtos,p)
        else:
            v+=0
    return round(v,2)