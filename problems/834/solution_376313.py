def media_matriz(matriz):
    '''funcao que dada uma matriz de inteiros nao vazia, retorna a media de todos
    os numeros da matriz, list->float'''
    soma=0
    for i in range(len(matriz)):
        soma=soma+sum(matriz[i])
    media=soma/(len(matriz)*len(matriz[0]))
    return round(media,2)