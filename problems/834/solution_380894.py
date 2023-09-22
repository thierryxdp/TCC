def media_matriz(matriz):
    '''Dado uma matriz, a função deve retornar a média de todos
    os números da matriz;
    list(list)->float'''
    
    soma=0
    n=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma+=matriz[i][j]
            n+=1
    
    media=(soma/n)
    return(round(media,2))