def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros de tamanho
qualquer, conta e retorna quantas vezes dado número aparece na matriz.'''
    #int, list -> int
    aparece = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                aparece += 1
    return aparece