def conta_numero(numero,matriz):
    '''Função que conta quantas vezes um numero aparece na matriz.
    list->int'''
    i=0
    for i in matriz:
        for j in i:
            if j==numero:
                i+=1
    return i