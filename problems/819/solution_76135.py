def filtraMultiplos(lista,n):
    '''descricao'''
    multiplos = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            multiplos = multiplos + (lista[proximo],)
        proximo = proximo + 1
    return multiplos