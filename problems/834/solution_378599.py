def media_matriz(matriz):
    """Dada uma matriz não vazia, retorna a 
    média dos numeros; list -> float """
    D = 0
    M = 0
    for i in matriz:
        for j in i:
            M += + j
            D += + 1
    return round((M/D), 2)