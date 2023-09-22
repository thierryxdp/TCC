def media_matriz(m):
    '''retorna a média de todos os números da matriz;
    mat->float'''
    
    soma=0
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma+=m[i][j]
            
    return round(soma/(len(m)*len(m[0]),2)