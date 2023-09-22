def media_matriz(matriz):
    """retorna a media da matriz
    list -> float"""
    
    matriz_soma = []
    
    for i in matriz:
        for j in matriz:
            a = matriz[i][j]
            matriz_soma.append(a)
    soma = sum(matriz_soma)
    
    qtd = matriz_soma.count
    
    
    return soma/qtd