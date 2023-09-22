def filtra_multiplos(lista,n):
    '''funcao que recebe uma lista e um numero e retorna outra lista
    list->list'''
    multiplos = []
    proximo = 0
    while proximo<len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + [lista[proximo]]
            proximo = proximo + 1
    return multiplos