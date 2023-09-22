def media_matriz(matriz):
    '''Essa funcao recebe uma matriz de inteiros NAO VAZIA e
    retorna a media de todos os numeros da matriz.
    matriz (int) -> float'''

    soma = 0
    qtd_numeros = len(matriz)*len(matriz[0])
    for linha in matriz:
        for numero in linha:
            soma = soma + numero
    media = round(soma/qtd_numeros,2)
    return media

#Casos de teste
# matriz = [[2,2,2],[2,2,2],[2,2,2]]
# media_matriz(matriz) == 2

# matriz2 = [[0,34,55,23],[-2,4,-10,-10],[-12,-10,76,3]]
# media_matriz(matriz2) == 12.58

# matriz3 = [[2,3,4], [1,-8,3]]
# media_matriz(matriz3) == 0.83

# matriz4 = [[-2,5],[3,5],[8,-9],[6,-1]]
# media_matriz(matriz4) == 1.88