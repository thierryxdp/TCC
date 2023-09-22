def total(lista, preco):
    '''Função que retorna o valor total dos itens da lista que estejam disponíveis na loja, list, dict -> float'''
    numero = 0
    for x in range(0, len(lista)):
        if lista[x] in dict.keys(preco):
            produto = [lista[x]]
            numero += preco([produto])
    return round(numero, 2)