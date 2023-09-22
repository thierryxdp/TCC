def total(lista,preco):
    compras=[]
    x=0
    while x < len(preco):
        if preco[x] in lista:
            list.append(compras,preco[x])
        x=x+1
    return round(sum(compras),2)