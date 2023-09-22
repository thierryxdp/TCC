def total(lista,precos):
    compras=[]
    for comprado in lista:
        if comprado in precos[comprado]:
            list.append(compras,precos[comprado])
    return compras