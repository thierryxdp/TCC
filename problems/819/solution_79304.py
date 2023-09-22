def filtraMultiplos(lista_num, n):
    '''Recebe uma lista de números e um número n e retorna
    uma lista com os múltiplos dele
    list, int -> list'''
    lista_mult = []
    i = 0
    while i < lista_num[-1]:
        if lista_num[i] % n == 0:
            lista_mult += lista_num[i]
        i += 1
    return list_mult