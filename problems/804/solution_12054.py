def filtra_pares(elementos):
    '''Retorna os elementos pares da tupla
    tupla-> tupla'''

    elementosPares = ()
    
    if elementos[0] % 2 == 0:
        elementosPares = elementosPares + (elementos[0],)
    if elementos[1] % 2 == 0:
        elementosPares = elementosPares + (elementos[1],)
    if elementos[2] % 2 == 0:
        elementosPares = elementosPares + (elementos[2],)
    if elementos[3] % 2 == 0:
        elementosPares = elementosPares + (elementos[3],)
    
    return elementosPares
#Start your python function here