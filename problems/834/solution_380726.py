def media_matriz(matriz):
    '''calcula e retorna a média de todosn os números da matriz
    	list->float'''
    
    media=0
    soma=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
             soma=soma+matriz[i][j]
    media=round((soma/(len(matriz)*len(matriz[0]))),2)
            
    return media