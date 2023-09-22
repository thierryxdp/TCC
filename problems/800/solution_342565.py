def total(lista_compra = [],produtos = {}):
    """Recebe uma lista de compras e um dicionário contendo o preço de cada
    produto disponível na loja. Retorna o valor total dos itens da lista que
    estão disponíveis na loja"""
    total = ()
    for pedido in produtos:
        if pedido in lista_compra:
            total = produtos[pedido]
    return round(sum(total),2)