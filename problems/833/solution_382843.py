def conta_numero(numero,matriz):
    '''dado um numero inteiro e uma matriz de tamanho qualquer, conta e retorna as aparições do numero na matriz.
    int,list-->int'''
    qntdd=0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j]==numero:
                qntdd=qntdd+1
    return qntdd