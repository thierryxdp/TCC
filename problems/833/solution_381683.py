def conta_numero(numero,matriz):
    '''Dado um número inteiro de tamanho qualquer, conta e retorna quantas vezes aquele número aparecerá na matriz; int,int -> int'''
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                soma=soma+1
    return soma