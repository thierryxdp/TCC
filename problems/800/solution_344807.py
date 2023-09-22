def total(lista,dicio):
    preco=0
    for x in lista:
        if x in dicio:
            preco=preco+dicio[x]

    return round(preco,2)