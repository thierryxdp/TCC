def total (lista_de_compras, produtos):
    ''' Função que recebe uma lista de compras e um dicionário contendo 
    cada produto preço com seu respectivo preço e que retorna o valor toal 
    dos produtos presentes na lista
    list, dict -> float'''
    preco = 0
    for item in lista_de_compras:
        if item in produtos:
            preco+= produtos[item]
    return round(preco, 2)