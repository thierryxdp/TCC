def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia, a função retorna a média
    de todos os números da matriz;
    list(list(int)) -> float"""
    qtd_numeros = 0
    soma_numeros = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            qtd_numeros = qtd_numeros + 1
            soma_numeros = soma_numeros + matriz[i][j]
    media = soma_numeros/qtd_numeros
    return round(media,2)