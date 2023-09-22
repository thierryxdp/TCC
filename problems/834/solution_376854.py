def media_matriz(matriz):
    """ essa função irá retornar a média de todos os numeros da matriz dada, e ira retornar um numero float com duas casas de precisão
entrada -> list
saida -> float """
    total = 0
    soma = 0
    for i in range(len(matriz)):
        total += len(matriz[i])
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
        media = round((soma/total),2)
    return media