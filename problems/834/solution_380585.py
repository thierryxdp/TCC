def media_matriz(matriz):
    '''
    Funçao que dada uma matriz de inteiros não vazia, retorna a media de todos os 
    numeros da matriz(com exatamente duas casas decimais de precisao)
    list(list) -> int
    '''
    media = 0
    i = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            media = media + matriz[i][j]
            i = i + len(matriz[i])
    return round(media/i,2)