def total(lista_compras,produto):
    """ Funçao que retorna o valor total dos itens da lista dada que
    estejam disponiveis em uma loja"""
    lista_compras = []
    produto = dict.items(produto)
    itens = 0
    for itens in lista_compras:
        if produto in lista_compras[itens]:
            lista_compras = lista_compras + dict.items(produto)
    return produto