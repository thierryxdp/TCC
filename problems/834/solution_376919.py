def media_matriz(matriz):
    '''Funcao que dada uma matriz de inteiros nao vazia, retorna a sua media.
    list -> int'''
    
    tamanho = len(matriz) * len(matriz[0])
    soma = 0
    
    for i in matriz:
        soma += sum(matriz[i])
    
    media = soma / tamanho
    
    return round(media, 2)