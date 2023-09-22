def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz, retorna quantas vezes aquele número aparece na matriz'''
    qnts = 0
    for i in len(matriz):
        for j in len(matriz[i]):
            if numero == matriz[i][j]:
                qnts = qnts + 1
    return qnts