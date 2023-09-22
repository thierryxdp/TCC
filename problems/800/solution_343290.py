def total(lista, preco):
    '''Função que retorna o valor total dos itens da lista que estejam disponíveis na loja, list, dict -> float'''
    numero = 0
    for x in range(0, len(lista)):
        produto = dict.keys(preco)
        if lista[x] in produto:
            numero = numero + produto
    return round(numero, 2)