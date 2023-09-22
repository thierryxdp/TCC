def media_matriz(matriz):
    '''funcao que retorna a media de todos os numeros da matriz'''
    soma=0
    for linha in matriz:
        soma+=sum(linha)
        media=soma/(len(matriz[1]*len(matriz))
        return round(media,2)