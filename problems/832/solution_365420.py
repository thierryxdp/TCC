def eh_quadrada(matriz):
    '''Retorna se a matriz é quadrada;list,list->bool''' 
    
    if (len(matriz)) != (len(matriz[0])):
        return False
    for i in range(len(matriz)):
        for j in range(i):
            if matriz[i][j] != matriz[j][i]:
                return False
        return True