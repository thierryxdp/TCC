def filtra_pares (numeros):
    '''int -> int'''
    tupla = ()
    
    for n in numeros:
        if n % 2 ==0:
            tupla.append(n)
            
    return tupla