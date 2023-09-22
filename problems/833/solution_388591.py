def conta_numero (n, matriz):
    '''Função que dado um número inteiro conta e retorna quantas vezes o número aparece na matriz
    int, matrix -> int'''
    soma = 0

    for i in matriz:
        soma += list.count(i,n)
    return soma