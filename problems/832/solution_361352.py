def eh_quadrada(matriz):
    '''funçao que identifica se uma matriz é quadrada e retorna um valor booleano'''
    '''list(list) -> bool'''
    i=0
    
    for i in range(matriz):
        cont_i=len(matriz)
        cont_j=len(matriz[i])
        i=i+1
        
    if cont_i == cont_j:
            return True
        
    else:
        if cont_i != cont_j:
                return False