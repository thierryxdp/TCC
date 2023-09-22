def media_matriz(matriz):
    """funcao que dada uma matriz de inteiros nao vazia, retorna a media de todos os numeros da matriz, com duas casas de precisao;
       list->float"""
    soma=0
    qtd_num=0
    media=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma=soma+matriz[i][j]
            qtd_num=qtd_num+1
    media=soma/qtd_num
    return round(media,2)