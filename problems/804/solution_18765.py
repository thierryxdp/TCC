def  filtra_pares(a, b, c, d):
    
    '''Função para determinar os ementos pares'''
    y = list(a, b, c, d)
   
    x = y % 2 == 0
    
    np = list(x)
    if y == x:
        return np
    else:
        return ( )