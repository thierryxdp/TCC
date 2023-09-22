def total(lista,preco):
    compras=[]
    x=0
    while x < len(lista):
        if lista[x] in preco.keys():
            list.append(compras,preco[lista[x]])
        x=x+1
    return round(sum(compras),2)