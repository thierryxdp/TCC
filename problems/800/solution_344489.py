def total(lista,prods):
    valor=0
    for i in lista:
        if lista[i] in prods:
            valor += prods[lista[i]]
    return round(valor,2)