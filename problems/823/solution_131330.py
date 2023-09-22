def faltante(pecas):
    """Esta função dada uma lista com N − 1 inteiros numerados de 1 a N,
    descubre qual número inteiro deste intervalo está faltando. O parâmetro 
    de entrada é uma lista L de tamanho N − 1 contendo números inteiros 
    (não repetidos) de 1 a N. A função deve retornar o número inteiro x que 
    pertence ao intervalo [1, N] mas que não pertence a lista de entrada L."""
    list.sort(pecas)
    if pecas[0] != 1:
        return 1
    lista = list(range(pecas[0],pecas[-1]+1))
    if lista == pecas:
        return pecas[-1] + 1
    i = 0
    while i < len(lista):
        if lista[i] != pecas[i]:
            return lista[i]
        i = i+1
    else:
        return i-