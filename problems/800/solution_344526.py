def total(compras, produtos):
    valor = 0
    lista_produtos = list(produtos.keys())

    for elemento in compras:
        if (elemento in lista_produtos):
            valor += produtos[elemento]

    return round(valor,2)