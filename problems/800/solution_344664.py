def total(lista=[],dict={}):
    '''Função que recebe uma lista de compras e um dicionário contendo o preço dos produtos disponíveis na loja e retorna o valro total dos itens da lista que estejam disponíveis na loja'''

    cont = 0.0
    for i in lista:
        cont+=dict[i]
    return round(cont,2)