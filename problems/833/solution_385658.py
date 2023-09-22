def conta_numero(numero,matriz):
    '''Funcao que retorna quantas vezes um numero aparece em uma matriz
       int, list -> int'''
    qnt = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                qnt = qnt + 1
    return qnt