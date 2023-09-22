def filtraMultiplos(lista, n):
    '''filtra os multiplos de n de uma lista
    lista, int -> lista'''
    multiplosN = []
    indice = 0
    while indice < len(lista):
        if lista[indice]%n == 0:
            multiplosN = multiplosN + (lista[indice],)
        indice = indice + 1
    return multiplosN