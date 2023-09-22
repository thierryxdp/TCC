def faltante(pecas):
    '''Funcao que,dada uma lista com N − 1 inteiros numerados de 1 a N,
    descubra qual numero inteiro deste intervalo está faltando.
    Entrada: O parametro de entrada e uma lista L de tamanho N − 1
    contendo numeros inteiros (não repetidos) de 1 a N.
    Saida: A funcao deve retornar o numero inteiro x que pertence ao
    intervalo [1, N] mas que nao pertence a lista de entrada L.
    list -> int'''
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