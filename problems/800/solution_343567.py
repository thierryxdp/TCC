def total (lista_compras, produtos):
    ''' Função que recebe uma lista de compras e um dicionário contendo 
    cada produto preço com seu respectivo preço e que retorna o valor toal 
    dos produtos presentes na lista
    list, dict -> float'''
    preco = 0
    for indice in lista_compras:
        if indice in produtos:
            preco+= produtos[indice]
    return round(preco, 2)