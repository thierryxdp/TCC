def total (lista,produtos):
    '''função que recebe uma lista de compras e um dicionário
    contendo o preço de cada produto disponível como entrada, 
    retornando o valor total dos itens da lista'''
    produtos = {}
    return sum(list(lista.values()))