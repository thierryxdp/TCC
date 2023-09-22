def total(lista,precos):
    compras=[]
    for comprando in lista:
        if comprando in precos:
            list.append(compras,precos[comprando])
    return round(sum(compras),2)