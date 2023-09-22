def media_matriz(matriz):
    """Funcao que calcula a media de todos os numeros de uma matriz
    de inteiros.
    Entrada: list(list);
    Saida: float;
    
    Parameters:
    matriz: lista com as listas para formar a matriz.
    """
    numeros = 0
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            numeros += 1
    media = round(soma/numeros, 2)
    
    return media