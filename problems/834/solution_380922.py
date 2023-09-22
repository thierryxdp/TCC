def media_matriz(matriz):
    '''função que calcula a média dos elementos de uma matriz
    list->float'''
    
    numeros=0
    qtd=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numeros=numeros+matriz[i][j]
            qtd=qtd+1
            
    media=numeros/qtd
    
    return round(media,2)