def filtraMultiplos(lista,numero):
    '''
    '''
    multiplos = []
    x = 0
    while x < len(lista):
        if lista[x] % numero == 0:
            multiplos = numero + lista[x]
    return multiplos