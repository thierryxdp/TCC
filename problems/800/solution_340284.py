def total(lista_compras, preco_produtos):
    '''Função que recebe uma lista de compras e um dicionário
    contendo como chaves os produtos de um supermercado e como 
    valores os preços deles, e retorna o valor total da compras
    arredondado para duas casas.
    [list], {dict} -> float'''
    total = 0
    for produto in lista_compras:
        total = total + preco_produtos[produto]
    return round(total,2)