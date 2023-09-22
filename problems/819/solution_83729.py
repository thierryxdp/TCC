def filtraMultiplos(lista,numero):
    '''
    '''
    lista =[]
    x=0
    while x < len(lista):
        if lista[x] % numero == 0:
            lista = numeros + lista[x]
        x = x + 1
    return lista