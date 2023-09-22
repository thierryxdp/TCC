def media_matriz(matriz):
    '''Função que dada uma matriz retornará a média da soma de todos os termos da matriz
    matrix -> float'''

    soma_colunas = 0

    if len(matriz) != 0:
        for linha in matriz:
          for coluna in linha:
            soma_colunas += coluna 
            media_colunas = soma_colunas / len(matriz[0])
          media_linhas = sum(linha) / len(matriz)
        media = (media_linhas+media_colunas)/2

    return round(media,2)

print(media_matriz([[7, 1, 2], [8, 2, 4], [2, 4, 6], [5, 1, 3]]))