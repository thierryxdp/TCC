def total(listaDeCompras, precoDosProdutos):
    """ Recebe uma lista de compras e um dicionário contendo o preço de cada produto e
    retorna o valor total dos itens da lista que estejam disponíveis 
    list, dict -> float """
    saida = 0
    for produto in listaDeCompras:
        if produto in precoDosProdutos.keys():
            saida+=precoDosProdutos[produto]
    return round(saida,2)