def conta_numero(numero,matriz):
    '''Conta e retorne quantas vezes um número aparece na matriz; int,list->int'''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            a=list.count(matriz,numero)
        return a