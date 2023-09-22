def total(lista,prods):
    valor=0
    for i in range(len(lista)):
        if lista[i] in prods:
            valor += prods[lista[i]]
            i+=1
    return round(valor,2)