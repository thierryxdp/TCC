import math
def total(lista, precos):
    '''Funçao que dada uma lista de compras e um dicionario contendo os preços dos produtos, irá retornar o valor total,
    list, dict -> float.'''
    soma = 0
    round(soma, 2)
    for i in lista:
        p=dict.get(precos, i)
        soma = soma + p
    
    return soma