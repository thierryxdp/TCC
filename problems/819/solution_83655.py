def filtraMultiplos(lista, n):
    '''Dada uma lista de números(n), a funcao filtra os múltiplos de n. 
    list,int->list'''

    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
            list.append(multiplos, lista[i])
        i = i + 1
    return multiplos