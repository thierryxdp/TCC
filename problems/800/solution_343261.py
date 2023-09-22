def total(lista, preco):
    '''Função que retorna o valor total dos itens da lista que estejam disponíveis na loja, list, dicionário -> float'''
    numero = 0
    lista_de_compras = {}
    for x in range(0, lista):
        if lista[x] in lista_de_compras:
            lista[x] += numero
    return round(numero, 2)