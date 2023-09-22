def total(lista,precos):
    """função que recebe uma lista de compras e um dicionario e retorna o valor total dos itens;lista-->dicionario"""
    compras=[]
    for comprado in lista:
        if  comprado in precos:
            list.append(compras,precos[comprado])
           
    return round(sum(compras),2)