def media_matriz(matriz):
    '''calcula a média de todos os elementos da matriz.
    list -> float'''

    cont = len(matriz) * len(matriz[0])
    soma = 0
    for i in matriz:
        for n in i:
            soma = soma + n

    media = round((soma/cont),2)
    return media