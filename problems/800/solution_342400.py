def total (lista, dic):
    ''' recebe uma lista de compras e um dicionário
    contendo o preço de cada produto disponível e 
    retorna o valor total dos itens da lista'''
    tot = 0
    for i in range(len(lista)):
        if lista[i] in dic:
            tot += dic[lista[i]]
    return tot