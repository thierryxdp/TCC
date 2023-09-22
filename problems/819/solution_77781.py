def filtraMultiplos(lista_numero, n):
    ''' funcao que recebe uma lista e um numero e retorna uma outra lista
    com todos os elementos original
list, int -> list'''
    lista = []
    i = 0
    while i < len(lista_numero):
        if lista_numero[i] % n == 0:
            lista = lista + [lista[i],]
            i = i + 1
    return lista