def total():
    'função que recebe lista de compras e dicionário com preço dos produtos e'
    'retorna valor total dos ítens que tem, disponíveis'
    produtos={'amaciante':4.99,'arroz':10.90,'biscoito':1.69,'café':6.98,'chocolate':3.79,'farinha':2.99,}
    return sum(dict.values(produtos))