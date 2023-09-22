def conta_numero (n, matriz):
    '''Função que dado um número inteiro conta e retorna quantas vezes o número aparece na matriz
    int, matrix -> int'''
    soma = 0
    linhas = matriz[0]
    colunas = matriz[1]

    for i in linhas:
        if i == n:
            soma += 1
    for i in colunas:
        if i == n:
            soma += 1
    return soma