def media_matriz(matriz):
    """Função que retorna a media da soma de todos os termos da matriz.
    list -> float """

    if matriz == []:
        soma_nula = 0

    else:
        soma = 0
        
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]

    if matriz == []:
        return soma_nula

    else:
        return round(soma/(len(matriz)*len(matriz[i])), 2)