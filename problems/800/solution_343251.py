def total(lista, preco):
    '''Função que retorna o valor total dos itens da lista que estejam disponíveis na loja, list, dicionário -> float'''
    numero = 0
    lista_de_compras = {}
    for x in range(len(lista), 0):
        if lista[x] in lista_de_compras:
            numero = lista + numero
        return round(numero, 2)