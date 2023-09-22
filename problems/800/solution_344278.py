def total(lista,dicionario):
    """funcao que recebe uma lista de compras e um dicionario contendo o preco de cada produto
    disponivel em uma determinada loja, e retorna o valor total dos itens da lista que estao
    disponiveis na loja
    list,dict -> float"""
    lista_loja = []
    for item in lista:
        if item in list(dict.keys(dicionario)):
            list.append(lista_loja,list(dict.values(dicionario)))
    return round(sum(lista_loja[0]),2)