def filtraMultiplos(lista,numero):
    '''
    '''
    multiplos = []
    x = 0
    while x < len(lista):
        if lista[x] % numero == 0:
            multiplos = [lista[x]]
        x = x + x[0:]
    return multiplos