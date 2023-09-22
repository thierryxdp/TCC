def media_matriz(matriz):
    """Função que, dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz
    entrada: list
    saída: float"""
    soma=0
    elem=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=soma+matriz[i][j]
            elem=elem+1
    return round(soma/elem,2)