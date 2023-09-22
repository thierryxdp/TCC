def eh_quadrada(matriz):
    ''' Função que verifica se é uma matriz quadrada ou não
    	True = Entrada é quadrada
        False = Entrada não é quadrada
        list(list)---->bool'''
    if matriz==[]:
        return True
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz)):              
                if len(matriz[0][:])==5  and range(len(matriz))==range(0, 5):
                    return True
                else:
                    return False