def media_matriz(matriz):
    '''Dado uma matriz, a função calculará 
    a média dos numeros que estejam presentes 
    nela com duas casas de precisão.
    list->float'''
    soma=0   
    valores=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma= soma+ matriz[i][j]
            valores= valores+1          
    media=soma/valores
    return round(media,2)