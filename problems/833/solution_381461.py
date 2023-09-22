def conta_numero(numero,matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros de tamanho
qualquer, conta e retorna quantas vezes aquele número aparece na matriz
    int, list -> int
    '''
    aparicoes = 0
    linhas = len(matriz)
    for i in range(linhas):
        colunas = len(matriz[i])
        for j in range(colunas):
            if matriz[i][j] == numero:
                aparicoes +=1
    return aparicoes