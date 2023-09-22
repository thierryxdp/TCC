def filtraMultiplos(lista,n):
    '''função que filtra os múltiplos de um número n'''
    multiplos = []
    for item in lista:
        if item%n==0:
            multiplos.append(item)
    return multiplos