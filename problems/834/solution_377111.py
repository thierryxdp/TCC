def media_matriz(matriz: list) -> float:
    """Retorna a média aritmética de todos os números de uma matriz de números
       inteiros não vazia

       Parameters:
       matriz: Lista de lista de números inteiros não vazia a ser analisada, na
       qual cada lista representa uma linha e cada lista de lista representa uma
       coluna

       Return:
       Dado o parâmetro "matriz", retorna a média aritmética de todos os números
       do parâmetro "matriz" com exatamente duas casas decimais de precisão

       Examples:
       media_matriz([[1, 1, 1], [1, 1, 1]]) == 1.0
       media_matriz([[2, 2], [2, 2]]) == 2.0
       media_matriz([[5, 7], [11, 4]]) == 6.75
    """

    numerador = 0
    denominador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numerador = numerador + matriz[i][j]
            denominador = denominador + 1

    resultado = numerador / denominador

    return round(resultado, 2)