def filtraMultiplos(l,n):
    '''dabjdanjadn'''
    multiplos = []
    proximo = 0
    while proximo < len(l):
        if l[proximo]%n == 0:
            multiplos.append(l[proximo])
        proximo = proximo +1
    return multiplos