def conta_numero(numero,matriz):
    '''retorna quantas vezes numero se repete dentro da matriz
    int,list->int'''
    vezes=0
    for sublist in matriz:
        for el in sublist:
            if el==numero:
                vezes=vezes+1
    return vezes