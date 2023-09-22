def total (l: list, d: dict)-> float:
    '''Retorna o valor total dos itens da lista que estejam disponíveis na
    loja, dada a lista de compras l e um dicionário d contendo o preço de 
    cada produto disponível na loja'''
    numero = 0
    for elem in l:
        if elem in list(d.keys()):
            numero = numero + d[elem]
    return round(numero, 2)