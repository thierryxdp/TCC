def total(lista_compra,produtos):
    """Recebe uma lista de compras e um dicionário contendo o preço de cada
    produto disponível na loja. Retorna o valor total dos itens da lista que
    estão disponíveis na loja"""
    valor_final = []
    for pedido in produtos:
        if pedido in lista_compra:
            list.append(valor_final,produtos[pedido])
    return round(sum(valor_final),2)