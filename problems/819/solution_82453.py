def filtraMultiplos(lista, num):
    '''
    Função que recebe uma lista e um número e retorna
    outra lista contendo os múltiplos do número informado
    list, int -> list
    '''
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % num == 0:
            m = lista[i]
            multiplos.append(m)
        i += 1
    return multiplos