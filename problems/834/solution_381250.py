def media_matriz(Matriz):
    '''retorna média números da matriz
    list->int/float'''
    
    i=0
    
    for x in range (len(Matriz)):
        for y in range len(Matriz[a]):
            i=i+Matriz[x][y]
    MediaMatriz=i/(len(Matriz)*len(Matriz[0]))
    
    return round(MediaMatriz,2)