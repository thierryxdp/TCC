def eh_quadrada(matriz):
    '''funcao que identifica se uma matriz dada como entrada e quadrada, retornando true se for e false se nao;
       list(list)-> bool'''
    matrizvazia= []
    if matriz== matrizvazia:
        return True
    else:
        for i in range(len(matriz)):
            i=i+0
            for j in range(len(matriz[i])):
                j=j+0
    if j == i:
         return True
    else:
         return False