def melhor_volta(matriz):
    '''Retorna uma tupla informando de quem foi a melhor volta, em quanto tempo e em que volta de acordo com os valores da matriz de entrada(6X10);
    list(list) -> tup'''
    j = 0
    i = 0
    tupla = (i,matriz[0][0],j)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j == 9:
                if matriz[i][j] < tupla[1]:
                    tupla = (i+1, matriz[i][j], j+1)
            else:
                
                if matriz[i][j] < tupla[1]:
                    tupla = (i+1, matriz[i][j], j+1)
                j=j+1
                
    return tupla