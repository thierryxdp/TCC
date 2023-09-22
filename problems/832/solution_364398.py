def eh_quadrada(m):
    '''funcao que verifica se uma matriz dada de entrada é quadrada;
    list -> bool'''
    lin = len(m)
    col = len(m[0])
    
    for i in range(lin):
        for j in range(col):
            if lin == col:
                return True
            for m[i][j] in range(0):
                return True
    return False