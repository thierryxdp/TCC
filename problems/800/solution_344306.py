def total (lista, dicionario):
    '''Função que retorna o valor total de itens de uma lista que estejam 
    disponíveis numa loja
    list, dict -> int'''
    soma = 0
    for c in lista:
        if c in dicionario:
            soma = soma + dicionario[c]
    return round(soma, 2)