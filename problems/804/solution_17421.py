def filtra pares(t):
    ''' docs '''
    nova_tupla = tuple ()
    
    if (t[0]%2) -- 0:
        nova_tupla = nova_tupla + (t[0],)
        
    if (t[1]%2) -- 0:
        nova_tupla = nova_tupla + (t[1],)
        
    if (t[2]%2) -- 0:
        nova_tupla = nova_tupla + (t[2],)
        
    if (t[3]%2) -- 0:
        nova_tupla = nova_tupla + (t[3],)
        
    return nova_tupla