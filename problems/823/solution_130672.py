def faltante(pecas):
    """dada uma lista com N-1 inteiros numerados de 1 a N,
    descubra qual numero inteiro deste intervalo está em falta.
    O prametro da entrada é uma lista L de tamanho N-1
    contendo numeros inteiros(sem repetição) de 1 a N. A
    funçao deve retornar o numero inteiro x que pertence ao
    intervalo [1,N] mas que não pertence a lista L
    list->int"""
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