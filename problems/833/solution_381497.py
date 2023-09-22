def conta_numero(numero, matriz):
    """Função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes 
    aquele número aparece na matriz
    int, list(list) -> int"""
    ocorrencias = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                ocorrencias += 1
    return ocorrencias