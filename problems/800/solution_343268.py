def total(lista, preco):
    '''Função que retorna o valor total dos itens da lista que estejam disponíveis na loja, list, dicionário -> float'''
    numero = 0
    lista_de_compras = {}
    for x in range(0, len(lista)):
        if lista[x] in lista_de_compras:
            valor = valor[lista[x]]
            numero = valor + numero
    return round(numero, 2)