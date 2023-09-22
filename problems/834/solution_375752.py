def media_matriz(matriz):
    """Função que calcula a qauntidade de vezes que se repete um nmuero dentro de uma matriz dados de entrada e retorna a quantidade de vezes
    int , list -> int"""
    total=0
    linha = 0
    coluna = 0
    for i in range(len(matriz)):
        linha = linha + 1
        for j in range(len(matriz[i])):
            total = total + matriz[i][j]
            coluna = coluna +1
    media = total /(linha*coluna)
    return media