def total(lista,dicionario):
    """ Função que recebe uma lista de compras e um dicionario contendo os preços de cada produto e retorna o valor da compra dos produtos da lista
    list, dic -> float """
    preco=0
    for produto in lista:
        if produto in dicionario:
            preco=preco+dict.get(dicionario,produto)
    return preco