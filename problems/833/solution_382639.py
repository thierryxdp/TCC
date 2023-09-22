def conta_numero(numero,matriz):
    """ conta quantas vezes um numero inteiro aparece em uma matriz de numeros inteiros;
    int, list -> int"""
    cont = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if matriz [x][y] == numero:
                cont = cont + 1
    return cont