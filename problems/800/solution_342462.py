def total(lista_de_compras, produtos):
    '''Função que recebe uma lista de compras e um dicionário com os preços dos produtos e retorna
    o preço total da lista
    list, dict -> float'''
    acumulador = 0
    for i in lista_de_compras:
        if i in produtos:
            acumulador += dict.get(produtos, i)
    return round(acumulador, 2)