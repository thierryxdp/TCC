def total(lista,prods):
    valor=0
    i=0
    for x in lista:
        if lista[i] in prods:
            valor += prods[lista[i]]
            i+=1
    return round(valor,2)