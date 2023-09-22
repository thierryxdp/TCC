def conta_numero(numero,matriz):
    '''conta a quantidade de vezes que um número aparece dentro da matriz
    list(list) -> int'''
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] = numero:
                total = total + 1
    return total