def faltante(lista):
    '''Verifica qual o número faltante numa lista de 1 até N com N-1 termos
    str --> int'''
    i = 0
    lista.sort()
    while i < len(lista):
        if lista[i]-1 not in lista and lista[i]-1 != 0:
            return lista[i]-1
        i += 1
    # caso o while rode a lista toda sem retornar, o elemento faltante do intervalo [1, N] será N
    return lista[-1]