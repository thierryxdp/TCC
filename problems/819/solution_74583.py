def filtraMultiplos(lista, n):
    '''dada uma lista e um numero n, retorna uma lista contendo olementos da lista que forem multiplos de n
    list, float -> list'''
    multiplos = []
    for i in lista:
        if i % n == 0:
            list.append(multiplos, i)
    return multiplos