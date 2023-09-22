def filtraMultiplos(lista, n):
    '''...'''
    multiplos= [ ]
    proximo = 0
    while lista[proximo]< len(lista):
        multiplos+= lista[proximo]
        proximo = proximo +1
        return multiplos