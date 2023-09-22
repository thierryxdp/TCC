def  filtra_pares(a, b, c, d):
    
    '''Função para determinar os ementos pares'''
    y = list(a, b, c, d)
   
    np = list(filter(lambda x: x % 2 == 0))
    
    t = [ ],[ ]
    
    
    t[0] =  int(input(np))% 2 == 0
    
    t[1] = int(input(np))% 2 != 0

    if y % 2 == 0:
        return t[0]
    else:
        return ( )