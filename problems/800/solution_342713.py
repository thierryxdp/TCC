def total(lista,produtos):
    '''função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja; list, dict -> int'''
    v=0
    for p in lista:
        if p in produtos:
            v+=dict.get(produtos,p)
        else:
            v+=0
    return round(v,2)