def eh_quadrada(matriz):
    ''' retorna um valor booleano identificando se a matriz é quadrada.
        Sendo uma matriz vazia, sendo quadrada.
        list --> bool'''
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[i]):
            return True
    else:
        return False
    
    if matriz == []
    return True