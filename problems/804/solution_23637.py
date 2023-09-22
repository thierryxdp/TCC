def filtra_pares(l):
    '''Função filtra os números pares de uma tupla
       int int int int --> int '''
    a, b, c, d = l
    l1 = ()
    if a % 2 == 0:
        l1 = l1 + (a,)  
    else:
        l1 = l1 
    if b % 2 == 0:
        l1 = l1 + (b,)
    else:
        l1 = l1
    if c % 2 == 0:
        l1 = l1 + (c,)
    else:
        l1 = l1
    if d % 2 == 0:
        l1 = l1 + (d,)
    else:
            l1 =l1
    return l1