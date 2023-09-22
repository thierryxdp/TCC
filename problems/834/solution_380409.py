def media_matriz(matriz):
    '''retorna a media dos elementos de uma matriz'''
    linhas = len(matriz)
    soma = 0
    tamanho = 0
    for a in range(0,len(matriz)):
        colunas = len(matriz[0])
        tamanho = linhas * colunas
        b=0
        while b < colunas:
            soma = soma + matriz[a][b]
            b+=1
    media = soma/tamanho
    return round(media,2)