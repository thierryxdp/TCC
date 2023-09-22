def total(lista,precos):
    compras=[]
    for comprado in lista:
        if  comprado in precos:
            compras= compras + precos[comprado]
           
    return compras