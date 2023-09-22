def faltante(pecas):
    '''Funcao que,dada uma lista com N 1 inteiros numerados de 1 a N,
    descubra qual numero inteiro deste intervalo esta faltando.'''
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
        return i-1