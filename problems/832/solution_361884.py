def eh_quadrada(m):
    '''verifica se m é uma matriz quadrada
    list -> bool'''
    
    if len(m) == 0 or len(m) == len(m[0]):
    	r = True
    else:
        r = False
        
    return r