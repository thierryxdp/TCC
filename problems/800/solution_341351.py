def total(lista,precos):
    compras=[]
    for comprado in lista:
        if  comprado in precos:
            list.append(compras,precos[comprado])
    c=0
    s=0
    while c < len(compras):
        compras=compras + compras[c]
           
    return compras