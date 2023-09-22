def total(lista_compras,produtos):
    '''Dados uma lista de compras e um dicionário contendo
    o preço de cada produto disponível em uma loja, retorna
    o valor total dos itens da lista que estejam disponíveis.
    list, dict -> float'''
    soma = 0
    for elemento in lista_compras:
        soma = soma + produtos[elemento]
    return soma