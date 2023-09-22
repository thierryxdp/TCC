def media_matriz (matriz):
    """Função que dado uma matriz de inteiros(matriz) não vazia, retorna
    a média de todos os números da matriz.
    lista -> float"""

    num = 0
    matrizLinhas = len(matriz[0])
    matrizColunas = len(matriz)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            num = num + matriz[i][j]
            

    return round(num/(matrizLinhas * matrizColunas), 2)