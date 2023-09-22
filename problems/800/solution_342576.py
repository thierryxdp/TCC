def total(lista_compras, preco_por_produto):
    '''Calcula o valor total dos produtos na lista de compras,
    a partir dos preços no dicionário
    list, dict --> float'''

    # variável para guardar o valor total do preço
    preco = 0

    # itera pela lista de compras
    for i in lista_compras:
        # verifica se o produto em i está no dicionário
        if i in preco_por_produto:
            # incrementa o preço referente ao produto em i à variável preco
            preco += preco_por_produto[i]
    return round(preco, 2)