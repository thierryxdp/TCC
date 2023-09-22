def filtra_pares (x):
    '''
    
    função que devolve apenas os números pares 
    tuple -> tuple
    '''
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    y = ()
    if (a % 2 == 0):
        y = y + x[0]
        if (b % 2 == 0):
            y = y + x[1]
            if (c % 2 == 0):
                y = y + x[2]
                if (d % 2 == 0):
                    y = y + x[3]