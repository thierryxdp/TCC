def conta_numero(numero, matriz):
    '''Retorna a quantidade de vezes que um número aparece numa matriz
    int, list -> int'''
    qntd = 0
        for i in len(matriz):
            for j in len(matriz[0]):
                if numero == matriz[i][j]:
                    qntd = qntd + 1
    return qntd