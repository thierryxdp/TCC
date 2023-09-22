def filtraMultiplos(lista,numero):
    '''
    '''
    lista =[]
    x=0
    while x < len(lista):
        if lista[x] % numero == 0:
            lista = numero + lista[x]
    return numero