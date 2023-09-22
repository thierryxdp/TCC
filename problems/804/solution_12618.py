def filtra_pares (numeros):
    '''int -> int'''
    tuple = ()
    
    for n in numeros:
        if n % 2 ==0:
            tuple.append(n)
            
    return tuple