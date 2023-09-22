def total(lista_de_compras,produtos):
    """ função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja
string -> int"""
    soma=0
    for x in lista_de_compras:
        if x in dict.keys(produtos):
            soma+=dict.get(produtos,x)
    return round(soma,2)