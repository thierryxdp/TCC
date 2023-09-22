def filtraMultiplos(lista, n):
    '''Função que, dado uma lista de números e um número (n),
    retorna outra lista contendo todos os elementos da lista
    original 
    list, int --> list'''

    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
            list.append(multiplos, lista[i])
        i = i + 1
    return multiplos