def filtraMultiplos(lista,numero):
    '''
    '''
    lista =[]
    x=0
    while x < len(lista):
        if lista[x] % numero == 0:
            numeros = numeros + lista[x]
        x = x + 1
    return numeros