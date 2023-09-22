def filtraMultiplos(x,n):
    '''Retorna uma lista contendo todos os elementos da lista
    de entrada que forem divisiveis por n.
    tuple --> tuple'''
    multiplos = []
    proximo = 0
    
    while proximo < len(x):
        if x[proximo]%n == 0:
            multiplos = multiplos + (x[proximo],)
        proximo = proximo + 1
    return multiplos