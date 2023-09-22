def total(lista, precos):
    '''Funçao que dada uma lista de compras e um dicionario contendo os preços dos produtos, irá retornar o valor total,
    list, dict -> float.'''
    soma = 0
    for i in lista:
        p=dict.get(precos, i)
        soma = soma + p
    round(soma,2)
    return soma