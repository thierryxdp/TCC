def filtraMultiplos(lista, num):
    '''
    Função que recebe uma lista e um número e retorna
    outra lista contendo os múltiplos do número informado
    list, int -> list
    '''
    i = 0
    M = []
    while i < len(lista):
        if lista[i] % num == 0:
            l = lista[i]
            M.append(l)
        i += 1
    return M