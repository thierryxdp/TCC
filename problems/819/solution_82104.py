def filtraMultiplos(lista, n):
    '''Filtra os multiplos de 'n' a partir de uma lista inicial'''
    multiplos= [ ]
    proximo = 0
    while proximo< len(lista):
        if lista[proximo] % n == 0:
            list.append (multiplos, lista[proximo])
        proximo +=1
    return