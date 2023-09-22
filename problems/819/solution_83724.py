def filtraMultiplos(lista,numero):
    '''
    '''
    numeros =[]
    proximo=0
    while proximo < len(lista):
        if lista % numero == 0:
            numeros = numeros + lista
    return numeros