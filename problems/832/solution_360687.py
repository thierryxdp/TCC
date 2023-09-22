def eh_quadrada(matriz):
    '''Dado uma matriz, essa função verificará 
    se é uma matriz quadrada. list->bool'''
    valores=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valores= valores+1
    if len(matriz)==0:
        return True
    elif (valores/len(matriz))== len(matriz):
        return True
    
    else:
        return False