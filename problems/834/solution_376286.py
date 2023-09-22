def media_matriz(matriz):
    "função que dada uma matriz de inteiros não vazia,retorna a média de todos os números dessa matriz.list->float."
    soma=0
    count =0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            count += 1
            x = soma/count    
    return round(x,2)