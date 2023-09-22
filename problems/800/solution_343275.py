def total(lista, preco):
    '''Função que retorna o valor total dos itens da lista que estejam disponíveis na loja, list, dict -> float'''
    numero = 0
    preco = {}
    for x in range(len(lista), 0):
        dict.keys(preco)
        if lista[x] in preco:
            valor = valor[lista[x]]
            numero = numero + valor
    return round(numero, 2)