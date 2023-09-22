def filtra_pares(x):
    (a, b, c, d) = x
    nova_tupla = ()
    if a%2 == 0:
    	nova_tupla + ((a,))
    if b%2 == 0:
        return nova_tupla + ((b,))
    if c%2 == 0:
        return nova_tupla + ((c,))
    if d%2 == 0:
        return nova_tupla + ((d,))
        
    
    return nova_tupla