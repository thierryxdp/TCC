def total (lista):
    '''função que recebe uma lista de compras e um dicionário
    contendo o preço de cada produto disponível como entrada, 
    retornando o valor total dos itens da lista'''
    produtos = {
        'amaciante':4.99,
        'arroz':10.90,
        'biscoito':1.69,
        'cafe':6.98,
        'chocolate':3.79,
        'farinha':2.99
    }
    return sum(list(lista.values()))