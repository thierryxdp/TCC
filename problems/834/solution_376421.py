def media_matriz(matriz):
    """Retorna a meda de todos os numeros da matriz;
       Entrada: list;
       Saida: float;
    """
    numeros = 0
    soma = 0
    for i in range (len(matriz)):
        for j in range (len(matriz[i]):
            soma += matriz[i][j]
            numeros += 1
    return round(soma/numeros, 2)