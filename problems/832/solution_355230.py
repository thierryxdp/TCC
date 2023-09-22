def eh_quadrada(m):
    '''funcao que identifica se uma matriz 
    é quadrada; list -> bool'''
    
    if len(m) == len(m[0]) or len(m) == len(m[0]) == 0 :
        return True
    else:
        return False