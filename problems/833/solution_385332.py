conta_numero(numero, matriz):
    '''Retorna quantas vezes um número aparece em uma matriz.
    int, list -> int'''
    acc = 0
    for i in len(matriz) - 1:
        for j in len(matriz[i]) -1:
            if numero == matriz[i][j]:
                acc += 1
    return acc