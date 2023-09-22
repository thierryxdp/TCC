def total(lista, preco):
    '''Função que retorna o valor total dos itens da lista que estejam disponíveis na loja, list, dict -> float'''
    numero = 0
    for x in range(0, len(lista)):
        if lista[x] in preco:
            produto = dict.keys(preco)
            numero += produto[lista[x]]
    return round(numero, 2)