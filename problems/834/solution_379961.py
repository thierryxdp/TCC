def media_matriz(matriz):
    '''
    	Funcao que recebe uma matriz de inteiros nao vazia e 
        retorna a media de todos os numeros da matriz
        list -> float
    '''
    soma = 0
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            soma = soma + matriz[i][j]
    media = soma/(qtd_linhas*qtd_colunas)
    return round(media, 2)