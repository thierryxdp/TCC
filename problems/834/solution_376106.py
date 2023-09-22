def media_matriz(matriz):
    """Retorna a média de todos os números da amtriz com 2 casas decimais de precisão; list -> float."""
    x = 0
    k = 0
    for i in range(0, matriz):
        k+= len(matriz[i])
        for j in range(0, matriz[i]):
            x+= matriz[i][j]
    return round(x/k,2)