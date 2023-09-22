def total(lista_compras, preco_produtos):
    produtos_compra = []
    for produtos in preco_produtos:
        if produtos in lista_compras:
            produtos_compra = produtos_compra + [lista_compras]
    return sum(produtos_compra)