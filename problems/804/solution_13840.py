def filtra_pares(a,b,c,d):
    '''
    função recebe uma tupla com quaro inteiros e retorne uma nova
    contendo apenas os elementos pares da tupla original;
    tuple -> tuple
    '''
    par1 = a
    par2 = b
    par3 = c
    par4 = d

    if (a%2 = 0):
        msg = par1
        
    if (b%2 = 0):
        msg = par2
        
    if (c%2 = 0):
        msg = par3
        
    if (d%2 = 0):
        msg = par4

    if (a%2 = 0) and (b%2 = 0):
        msg = par1, par2

    if (a%2 = 0) and (b%2 = 0) and (c%2 = 0):
        msg = par1, par2, par3
        
    if (a%2 = 0) and (b%2 = 0) and (c%2 = 0) and (d%2 = 0):
        msg = par1, par2, par3, par4

    return msg