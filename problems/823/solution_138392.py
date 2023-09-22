def faltante(pecas_joao):
    '''Função que recebe uma lista com N − 1 inteiros numerados de 1 a N,
    e retorna qual número inteiro deste intervalo está faltando.
    list -> int'''
    list.sort(pecas_joao)

    if pecas_joao[0] != 1:
        return 1

    lista = list(range(pecas_joao[0],pecas_joao[-1]+1))
    if lista == pecas_joao:
        return pecas_joao[-1] + 1

    i = 0
    while i < len(lista):
        if lista[i] != pecas_joao[i]:
            return lista[i]

        i = i+1

    else:
        return i-1