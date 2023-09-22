def conta_numero(numero,matriz):
    '''Função que retorna quantas vezes o número dado na entrada aparece
    na matriz dada de entrada também
    int, list -> int'''
    conta = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                conta = conta + 1
    return conta