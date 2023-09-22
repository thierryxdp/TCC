def filtra_pares (n):
    '''int -> int'''
    pares = []
    
    for n in numeros:
        if n % 2 ==0:
            pares.append(n)
            
    return pares