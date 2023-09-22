def filtraMultiplos(lista, n):
    '''função que filtra os múltiplos de um número, dada uma lista e um número'''
    multiplos = []
    proximo = 0
    while proximo < len (lista):
        if lista[proximo]%n==0:
            multiplos.append(lista[proximo])
        proximo = proximo +1
    return multiplos