def total(lista=[], produtos={}):
    '''Função que dada um lista de compras e um dicionário com preços,
retorna o valor total dos itens da lista
list, dici -> '''
    lista = ['biscoito', 'chocolate', 'farinha']
    produtos = {'amaciante':4.99, 'arroz':10.90, 'biscoito':1.69, 'cafe':6.98, 'chocolate':3.79, 'farinha':2.99}
    acum = 0
    for i in lista:
        acum += produtos[i]
    return round (acum)