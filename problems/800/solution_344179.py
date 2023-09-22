#EXEMPLO: lista de compras = ['biscoito', 'chocolate', 'farinha']
#produtos = {'amaciante':4,99, 'arroz':10,90, 'biscoito':1,69, 'cafe':6,98,
#'chocolate':3,79, 'farinha':2,99}
#O valor retornado da função será 8.47
def total(lista,dicionario):
    """Função que recebe uma lista de compras e um dicionário contendo
    o preço de cada produto disponível em uma determinada loja, e retorna
    o valor total dos itens da lista que estejam disponíveis nesta loja;
    list, dict -> float"""
    cont = 0.0
    for i in lista:
        cont = dict[i]
    return round(cont,2)