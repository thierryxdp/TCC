def conta_numero(numero,matriz):
    
    '''
    '''
    vezes=0
    for x in range(len(matriz)):
        vezes=vezes+matriz.count(numero)
    return vezes