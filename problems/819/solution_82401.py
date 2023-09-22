def filtra_multiplos(lista_numeros, n):
    '''Filtra uma lista de numeros, retornando apenas os ques são múltiplos de n
    list, int --> list'''
    i = 0
    lista = []
    while i < len(lista_numeros):
        if lista_numeros[i] % n == 0:
            lista.append(lista_numeros[i])
        i += 1
    return lista