def eh_quadrada(matriz):
    '''Programa que retorna se a matriz é quadrada ou não
    list -> bool'''
    i = len(matriz)
    j = 0
    if i > 0:
        for j in range(len(matriz[j])):       
            j = j+1    
        return i == j
    else:
        return True