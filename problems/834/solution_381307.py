def media_matriz(matriz):
    '''funcao que recebe uma matriz de numeros inteiros e 
    retorna a media deles'''
    soma=0
    for linha in matriz:
        soma += sum(linha)
    media=soma/(len(matriz[1])*len(matriz))
    
    return round(media,2)