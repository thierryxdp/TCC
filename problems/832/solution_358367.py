def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada ou não.
    list -> bool'''    
    if matriz == []:
        return True
    for i in matriz:
        if len(i) == len(matriz):
            return True
        else:
            return False