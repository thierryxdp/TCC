def total(lista,precos):
    '''funcao que retorna a soma de precos com itens correspondentes a uma lista.'''
    '''dic=>float'''
    compras=[]
    for comprado in lista:
        if  comprado in precos:
            list.append(compras,precos[comprado])
           
    return round(sum(compras),2)