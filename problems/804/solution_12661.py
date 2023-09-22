def filtra_pares (numeros):
    '''tuple -> tuple'''
    pares = ()
    
    for n in numeros:
        if n % 2 ==0:
            pares.append(n)
            
    return pares