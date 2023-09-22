def conta_numero(numero, matriz):

    '''Função que dado um número inteiro e uma matriz de inteiros de tamanho
qualquer, conta e retorna quantas vezes aquele número aparece na matriz.
int, list -> int'''
    
    i = 0
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if matriz[linha][coluna] == numero:
                i += 1
    return i