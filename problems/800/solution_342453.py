def total(lista,preco):
    compras=[]
    for i in preco:
        if lista[i] in preco:
            list.appen(compras,preco[lista[i]])
    return round(sum(compras),2)