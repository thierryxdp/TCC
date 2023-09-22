def total(lista,precos):
    '''função que retorna a soma dos produtos listados; dic => float'''
    compras=[]
    for comprado in lista:
        if comprado in precos:
            list.append(compras,precos[comprado])
    return round(sum(compras),2)