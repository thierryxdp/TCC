def total(lista, dic):
    '''Função que recebe uma lista de compras e um dicionário contendo o preço
de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que
estejam disponíveis nesta loja;
       list, dict --> float'''
    a = []
    for x in lista:
        if x in dic:
            list.append(a, dic[x])
            b = sum(a)
    return round(b,2)