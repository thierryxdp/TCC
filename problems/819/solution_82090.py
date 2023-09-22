def filtraMultiplos(lista, n):
    '''...'''
    multiplos= [ ]
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
        list.append(lista[proximo])
        #multiplos = (lista [proximo], )
        proximo +=1
    return multiplos