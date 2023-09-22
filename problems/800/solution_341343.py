def total(lista,precos):
    compras=[]
    for comprado in lista:
        if  comprado in precos:
            list.append(compras,comprado)
            compras=comprado.values()
    return compras