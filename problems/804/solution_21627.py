def filtra_pares(tupla):
    
    if tupla[0] % 2 == 0:
        
        a = tupla [0]
    
    else:
        
        a = None

    if tupla[1] % 2 == 0:
        
        b = tupla [1]
    
    else:
        
        b = None

    if tupla[2] % 2 == 0:
        
        c = tupla [2]
    
    else:
        
        c = None

    if tupla[3] % 2 == 0:
        
        d = tupla [3]
    
    else:
        
        d = None
        
    nova_tupla = a, b, c, d
    
    return nova_tupla

filtra_pares((147,613,609,267))