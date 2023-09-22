def conta_numero(numero,matriz):
    ''' quanta a quantidade de vezes que um determinado numero aparece na matriz'''
    K = 0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == numero:
                K += 1 
    return K