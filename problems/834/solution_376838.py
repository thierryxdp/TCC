def media_matriz(matriz):
    """
    Função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz (com duas casas decimais de precisão).
    list -> float
    """
    media = 0

    # caso seja uma matriz linha
    if type(matriz[0]) == int:
        media = sum(matriz)/len(matriz)
    
    # caso contrário
    else:
        total_elementos = 0
        for i in range(len(matriz)):
            media += sum(matriz[i])
            total_elementos += len(matriz[i])
        media /= total_elementos
    
    return round(media,2)