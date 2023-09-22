def tota(lista,preco):
    compras=[]
   
    for i in len(preco)-1:
        if lista[i] in preco:
            list.appen(compras,preco[lista[i]])
    return round(sum(compras),2)