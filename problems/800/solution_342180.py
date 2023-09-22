def total(lista_de_compras, produtos):
    '''Função que recebe uma lista de compras com um dicionário contendo o preço de cada produto
, e retorna o valor total dos intens que estão disponíveis nesta loja.; list, dict -> float'''
    acumulador = 0
    for i in lista_de_compras:
        if i in produtos:
            acumulador += dict.get(produtos, i)
    return round(acumulador, 2)