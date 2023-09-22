def filtraMultiplos(lista,numero):
    '''
    '''
    numeros =[]
    proximo=0
    while proximo < len(lista):
        if lista[proximo] % numero == 0:
            numeros = numeros + lista[proximo]
    return numeros