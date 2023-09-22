def total(lista_compras, dicionario_preco):
    """
    Essa função recebe uma lista de compras, um dicionario com 
    o preço e o nome do produto e retorna o valor total dos itens 
    da lista disponíveis na loja.
    list, dict -> float
    """
    preco = 0
    for i in dicionario_preco.keys():
        for x in lista_compras:
            if x in i:
                preco += dicionario_preco[i]
    return round(preco, 2)