def media_matriz(matriz):
    """Essa função recebe uma matriz e retorna a media da mesma
    list -> int"""
    numero_elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero_elementos += 1
    return sum(matriz)/numero_elementos