def total(lista, preco):
    '''Função que retorna o valor total dos itens da lista que estejam disponíveis na loja, list, dict -> float'''
    numero = 0
    produto = dict.keys(preco)
    for x in range(0, len(lista)):
        if lista[x] in produto:
            numero = numero + produtos
    return round(numero, 2)