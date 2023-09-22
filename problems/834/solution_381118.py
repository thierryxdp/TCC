def media_matriz(matriz):
    """Essa função recebe uma matriz e retorna a media da mesma
    list -> int"""
    soma_matriz = 0
    numero_elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma_matriz += matriz[i][j]
            numero_elementos += 1
    return round(soma_matriz/numero_elementos,2)