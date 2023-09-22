def media_matriz(matriz):
    '''Recebe uma matriz de inteiros nao vazia e retorna
    a media de todos os numeros da matriz;
    list -> float'''
    i=0
    soma=0
    for m in matriz:
        for n in m:
            soma+=n
            i+=1
    return round((soma/i),2)