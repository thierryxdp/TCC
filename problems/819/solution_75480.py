def filtraMultiplos (lista, n):
    '''Função retorna os múltiplos de n contidos na lista.
    int -> list'''
    indice = 0
    lista_multiplos = []
    while indice < len(lista):
        if lista[indice] % n == 0:
            list.append (lista_multiplos,lista[indice])
        indice = indice + 1
    return lista_multiplos