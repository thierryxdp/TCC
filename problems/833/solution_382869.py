def conta_numero(numero,matriz):
    '''dado um numero inteiro e uma matriz de tamanho qualquer, conta e retorna as aparições do numero na matriz.
    int,list-->int'''
    qntdd=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero==matriz[i][j]:
                qntdd=qntdd+1
    return qntdd