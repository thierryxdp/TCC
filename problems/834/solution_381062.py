def media_matriz(matriz):
    '''Função que dada uma matriz retornará a média da soma de todos os termos da matriz
    matrix -> float'''

    linha = len(mat)
    coluna = len(matriz[i])

    for i in matriz:
        if len(matriz) != 0:
            media_linhas = sum(linhas)/len(linhas)
            media_colunas = sum(colunas)/len(colunas)
            media = (media_linhas+media_colunas)/2

        return round(media,2)