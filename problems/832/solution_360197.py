def eh_quadrada(m):
    '''indentifica se uma matriz eh quadrada
    list -> bool'''
    
    if len(m)==0 or len (m)==len(m[0]):
        return True
    else:
        return False