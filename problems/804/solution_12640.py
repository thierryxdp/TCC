def filtra_pares (n):
    '''tuple -> int'''
    pares = []
    
    for n in n:
        if n % 2 ==0:
            pares.append(n)
            
    return pares