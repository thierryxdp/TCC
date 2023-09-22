def total(lista_compras, dict_preco):
    '''Recebe uma lista de compras e um dicionário contendo
       o preço dos produtos disponíveis, e retorna o valor total
       da compra da lista;
       list, dict -> float'''
    compra = 0
    for item in lista_compras:
        if item in dict.keys(dict_preco):
            compra += dict_preco[item]
    return compra