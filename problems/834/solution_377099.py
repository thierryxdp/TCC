def media_matriz(matriz):
    """Recebe uma matriz de inteiros não vazia e retorna a
       média de todos os elementos da matriz
       parâmetros de entrada:list(list)
       parâmetros de saída:float"""
    soma=0
    elemento=0
    media=soma/len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=soma+elemento
        media=soma/len(matriz)
    return media