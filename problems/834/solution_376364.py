def media_matriz(matriz:list) -> float:
    """Função que irá calcular a média de todos os valores de uma matriz.

        Parameters:
        matriz: matriz não vazia formada por valores inteiros

        Returns:
        média de todos os valores da matriz com duas casas decimais de precisão

        list -> float
    """

    media = 0
    for i in range(len(matriz)):
        media_por_linha = sum(matriz[i]) / len(matriz[i])
        media = (media + media_por_linha)
    return round((media/len(matriz)), 2)