def media_matriz(matriz):
    '''Retorna a média de todos os números da matriz com duas casas decimais
list -> float'''
    linhas=len(matriz)
    colunas=len(matriz[0])
    qtd_termos=linhas*colunas
    soma_termos=0
    for i in range(linhas):
        for j in range(colunas):
            soma_termos=soma_termos+matriz[i][j]
    media=soma_termos/qtd_termos
    return round(media,2)