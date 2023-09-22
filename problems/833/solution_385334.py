def conta_numero(numero, matriz):
    '''Retorna quantas vezes um número aparece em uma matriz.
    int, list -> int'''
    acc = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if numero == matriz[i][j]:
                acc += 1
    return acc