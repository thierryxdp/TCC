def media_matriz(matriz):
    #Função que dada uma matriz de inteiros não vazios
    #retorna a média de todos os números da matriz
    lin = len(matriz)
    col = len(matriz[0])
    soma = 0
    x = -1
    for i in matriz:
        x += 1
        for j in matriz[x]:
            soma += j
    return round(soma / (lin*col), 2)