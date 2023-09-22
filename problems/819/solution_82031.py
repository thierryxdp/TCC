def filtraMultiplos(lista, n):
    '''...'''
    multiplos = []
    proximo = 0
    while proximo <len (n):
        if n[proximo]%n == 0:
            multiplos = multiplos + (n [proximo], )
            proximo = proximo +1
            return multiplos