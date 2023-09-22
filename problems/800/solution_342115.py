def total(lista,disponivel):
    '''Função que calcula e retorna o valor total dos produtos da lista
    de entrada, caso estejam incluidos no dicionário de entrada disponivel
    list, dict -> float'''
    soma = 0
    i = 0
    while i<len(lista):
        a = produto[lista[i]]
        soma = soma + a
        i = i + 1
    return round(soma,2)