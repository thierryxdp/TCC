def filtraMultiplos (lista, n):
    '''Retorna uma nova lista com os elementos da lista "lista" inserida que sejam múltiplos do número "n" inserido;
    list, int -> list'''
    lista_result = []
    for elem in lista:
        if elem % n == 0:
            lista_result.append(elem)
    return lista_result