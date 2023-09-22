def media_matriz(matriz):
    """Função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz com duas casas 
    decimais de precisão
    list(list) -> float"""
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    qtd_numeros = len(matriz)*len(matriz[0])
    media = round(soma / qtd_numeros, 2)
    return media