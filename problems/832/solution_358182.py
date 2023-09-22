def eh_quadrada(matriz):
    ''' Dada uma matriz, a função retorna
        se a matriz é quadrada ou não
        list -> bool'''
    if matriz==[]:
        return True    
    if len(matriz) == len(matriz[0]):
        return True
    else: 
        return False