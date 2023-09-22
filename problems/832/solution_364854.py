def eh_quadrada(matriz):
    '''função que recebe uma matriz e verifica se ela é quadrada
    list-> bool'''
    
    zeros=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j]==0:
                zeros=zeros+1
            
    if zeros==(len(matriz)):
        return True
    else:
        return False