def media_matriz(matriz): #Entrada: int e matriz (list)
    soma = 0
    num_linha = len(matriz)
    num_coluna = len(matriz[0])
    for linha in matriz:
        for coluna in linha:
            soma += coluna
    media = soma / num_linha * num_coluna #A função soma todos os números da matriz e divide pela quantidade de casas na matriz.
    media = round(media, 2)
    return media #Saída: int