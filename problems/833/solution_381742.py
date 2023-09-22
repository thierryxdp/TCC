def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz, retorna quantas vezes aquele número aparece na matriz
    int, list -> int'''
    qnts = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
        for i in len(linhas):
            for j in len[matriz[0]]:
                if numero == matriz[i][j]:
                qnts = qnts + 1
        return qnts