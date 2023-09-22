def conta_numero(numero,matriz):
    '''retorna quantas vezes um numero aparece na matriz
    int,matriz -> int'''
    cont = 0
    for L in range(len(matriz)):
        for P in range(len(matriz[L])):
            if matriz[L][P] == numero:
                cont += 1
        return cont