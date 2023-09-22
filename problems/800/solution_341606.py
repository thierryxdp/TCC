def total(lista_compras, preco_produtos):
    produtos_compra = []
    for produtos in lista_compras:
        if produtos in preco_produtos:
            produtos_compra = produtos_compra + produtos
    return produtos_compra