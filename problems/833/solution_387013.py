def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz,
    retorna quantas vezes aquele número aparece
    na matriz.
    int, list -> int'''
    qnt = 0
    for i in range(len(matriz)) :
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                qnt += 1
    return qnt