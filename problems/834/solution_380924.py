def media_matriz(matriz):
    '''Função que retorna a média dos números de uma matriz
    
    list->float'''
    
    numeros = 0
    qntd = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numeros = numeros + matriz[i][j]
            qntd = qntd+1
            
    media = numeros/qntd
    
    return round(media,2)