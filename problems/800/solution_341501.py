def total(lista, dicionario):
    '''
    recebe uma lista de compras e um dicionario com o preco 
    de cada item e retorna o total das compras
    list, dict->float
    '''
    preco=0
    for i in lista:
        if i in dicionario:
            preco=preco + dict.get(dicionario,i)
    return round(preco,2)