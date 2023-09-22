def total (lista_compras= [], preco_produtos= {}):
    """Função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja.
    list, dict -> float"""
    cont = 0.0
    for i in lista_compras:
        cont += preco_produtos[i]
    return round(preco_produtos, 2)