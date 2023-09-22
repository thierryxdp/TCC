def total(lc, dp):
    """Função que recebe uma lista de compras e um dicionário
    de preços e retorna o valor total dos itens da lista;
    list, dict -> int."""
    lista_de_compras = ['biscoito', 'chocolate', 'farinha']
    produtos = { 'amaciante':4.99, 'arroz':10.90,
                'biscoito':1.69, 'cafe':6.98, 
                 'chocolate':3.79, 'farinha':2.99 }
    for e in lc:
        r = dict.get(dp,e,0)
        ret = sum(r)
        round(ret, 2)
    return ret