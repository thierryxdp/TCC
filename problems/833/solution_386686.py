def conta_numero(n,matriz):
    '''Função que dado um numero inteiro e uma matriz, conta e retorna quantaz vezes esse numero aparece na matriz
    list,int -> int'''
    cnt = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == n:
                cnt = cnt + 1
    return cnt