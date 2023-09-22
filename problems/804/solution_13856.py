def filtra_pares(a,b,c,d):
    '''
    função recebe uma tupla com quaro inteiros e retorne uma nova
    contendo apenas os elementos pares da tupla original;
    tuple -> tuple
    '''
    
    if (a%2 == 0):
        msg = (a)
        
    if (b%2 == 0):
        msg = (b)
        
    if (c%2 == 0):
        msg = (c)
        
    if (d%2 == 0):
        msg = (d)
        
    if (a%2 == 0) and (b%2 == 0):
        msg = (a, b)

    if (a%2 == 0) and (b%2 == 0) and (c%2 == 0):
        msg = (a, b, c)
        
    if (a%2 == 0) and (b%2 == 0) and (c%2 == 0) and (d%2 == 0):
        msg = (a, b, c, d)

	return msg