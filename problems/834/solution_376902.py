def media_matriz(matriz):
    '''funcao que dada uma matriz de inteiros nao vazia, retorna a media de todos os numeros com duas casas decimais
       matriz(int) -> float'''
    qnt_elem = len(matriz) * len(matriz[0])
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            media = media + matriz [i][j]
    media = media/qnt_elem
    return round(media)