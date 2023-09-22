def media_matriz(matriz):
    """Função que retorna a média de uma dada matriz. list -> int"""
    soma_matriz = 0
    numero_elementos = 0
    for m in range(len(matriz)):
        for n in range(len(matriz[m])):
            soma_matriz += matriz[m][n]
            numero_elementos += 1
    return round(soma_matriz/numero_elementos,2)