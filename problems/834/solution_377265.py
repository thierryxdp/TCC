def media_matriz(matriz):
    '''retorna dado uma matriz a media de todos 
    os numeros pertencentes a mesma
    list->float'''
    Nelementos=len(matriz)*len(matriz[0])
    somatotal=0
    for i in range(len(matriz)):
        soma=0
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
        somatotal+=soma
    return round(somatotal/Nelementos,2)