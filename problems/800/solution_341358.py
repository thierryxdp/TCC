def total(lista,precos):
    compras=[]
    for comprado in lista:
        if  comprado in precos:
            list.append(compras,precos[comprado])
        compras=sum(compras)
    return round(compras,2)