def total(lista_de_compras, produtos):
    """Função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja
    e fornece o valor total dos itens da lista que estejam disponíveis nessa loja
    list, dict -> float"""
    acumulador = 0
    for i in lista_de_compras:
        if i in produtos:
            acumulador += dict.get(produtos, i)
    return round(acumulador, 2)