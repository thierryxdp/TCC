def conta_numero(numero:int, matriz:list) -> int:
    """Essa função, dada uma matriz de números inteiros de tamanho qualquer
    e um número inteiro, retorna a quantidade de vezes que o número
    aparece na matriz"""
    
    vezes = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                vezes += 1
    
    return vezes