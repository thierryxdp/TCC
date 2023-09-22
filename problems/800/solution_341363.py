def total(lista,produtos):
    '''retorna o valor total dos itens que estão disponíveis na loja'''
    ''''list, dict -> float'''

    compras=[]
    for comprado in lista:
        if  comprado in precos:
            list.append(compras,precos[comprado])
           
    return round(sum(compras),2)