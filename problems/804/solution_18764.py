def  filtra_pares(a, b, c, d):
    
    '''Função para determinar os ementos pares'''
    y = list(a, b, c, d)
    t = int(input(y))
    a = int(input(y % 2))
    b = int(input(y % 2))
    c = int(input(y % 2))
    d = int(input(y % 2))
    
    x = y % 2 == 0
    
    if y == x :
        return x
    else:
        return ( )