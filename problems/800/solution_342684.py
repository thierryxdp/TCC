def total(lista_compras, precos):
    """A função recebe como entrada uma lista contendo strings,
    que corresponde a uma lista de compras, e um dicionário
    cujas chavez são os produtos e os valores são os preços dos
    produtos, e retorna o valor total (float) dos itens da lista
    de compras."""
    for produto in lista_compras:
        total += precos[produto]
    return total