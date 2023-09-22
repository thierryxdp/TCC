def total(lista, dic):
    '''recebe uma lista de compras e um dicionario contendo o preço dos produtos disponivel na loja  e retorna o valor total da conta.list,dict->float'''
    valor=0
    for produto in range(len(lista)):
        x = lista[produto]
        if x in dict.keys(dic):
            valor+=dict.get(dic,x)
    return round(valor,2)