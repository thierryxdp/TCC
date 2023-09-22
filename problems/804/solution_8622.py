def filtra_pares(tupla):
    ''' Avalia e retorna os números pares de uma tupla, dada como valor de entrada, em forma de tupla
        tupla -> tupla'''
    
    tupla_par = ()
    
    for n in tupla:
        
        if n % 2 == 0:
            
            tupla_par += n,
            
    return tupla_par