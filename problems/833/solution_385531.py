def conta_numero(numero, matriz):
    '''Função que recebe um número inteiro e uma matriz de números
    inteiros e retorna a quantidade de vezes que aquele número aparece
    na matriz.
    int, list -> int'''
    contador = 0
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    for i in range(n_linhas):
        for j in range(n_colunas):
            if matriz[i][j] == numero:
                contador = contador + 1
    return contador