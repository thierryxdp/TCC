def total(lista_compras, preco_por_produto):
    '''Calcula o valor total dos produtos na lista de compras,
    a partir dos preços no dicionário
    list, dict --> float'''
    preco = 0
    for i in lista_compras:
        if i in preco_por_produto:
            preco += preco_por_produto[i]
    return round(preco, 2)