def total(x,y):
    """função que recebe uma lista de compras e um dicionario contendoo preço de cada produto disponivel em uma determinada loja e retorna o valor dos itens da lista que estejam disponiveis nesta loja;list->int"""
    proximo = 0
    contador = 0
    for x in y:
        if x in y[proximo]:
            proximo = proximo + 1
            contador = contador + codict.get(y,proximo)
        return contador