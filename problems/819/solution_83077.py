def filtraMultiplos(lista, n):
    '''
    Função que recebe uma lista e um número e retorna
    outra lista contendo os múltiplos do número (n) informado
    list, int -> list
    '''
    i = 0
    M = []
    while i < len(lista):
        if lista[i] % n == 0:
            l = lista[i]
            M.append(l)
        i += 1
    return M