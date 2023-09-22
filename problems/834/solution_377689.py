def media_matriz(matriz: list)-> float:
    """Dada uma matriz de inteiros não vazia, a função retorna a média
    de todos os números da matriz, com duas casas decimais de precisão"""
    contador = 0
    numlinhas = len(matriz)
    numcolunas = len(matriz[0])
    for i in range(numlinhas):
        for j in range(numcolunas):
            contador += matriz[i][j]
    return round(contador/(numlinhas*numcolunas), 2)