def media_matriz(matriz):
    '''funcao que dada uma matriz de inteiros nao vazia, retorne a media 
    de todos os numeros da matriz, int->int'''
    soma=0
    for l in range(len(matriz)):
        soma=soma+sum(matriz[l])
    media=soma/(len(matriz)*len(matriz[0]))
    return round(media,2)