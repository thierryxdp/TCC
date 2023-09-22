def conta_numero(numero,matriz):
    '''Função que conta quantas vezes um numero aparece na matriz.
    list->int'''
    i=0
    for elemento in matriz:
        if elemento == numero:
            i+=1
    return i