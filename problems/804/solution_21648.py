def filtra_pares(tupla):
    
    if tupla[0] % 2 == 0 and tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
        
        nova_tupla = tupla[0], tupla[1], tupla[2], tupla[3]
        
        return nova_tupla
        
    elif tupla[0] % 2 != 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 != 0:
        
        nova_tupla = ()
        
        return nova_tupla
    
    elif tupla[0] % 2 == 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 != 0:
        
        nova_tupla = tupla[0],
        
        return nova_tupla
    
    elif tupla[0] % 2 != 0 and tupla[1] % 2 == 0 and tupla[2] % 2 != 0 and tupla[3] % 2 != 0:
        
        nova_tupla = tupla[1],
        
        return nova_tupla

    elif tupla[0] % 2 != 0 and tupla[1] % 2 != 0 and tupla[2] % 2 == 0 and tupla[3] % 2 != 0:
        
        nova_tupla = tupla[2],
    
        return nova_tupla
        
    elif tupla[0] % 2 != 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 == 0:
        
        nova_tupla = tupla[3],
        
        return nova_tupla

    elif tupla[0] % 2 == 0 and tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 != 0:
        
        nova_tupla = tupla[0], tupla[1], tupla[2]
        
        return nova_tupla
    
    elif tupla[0] % 2 == 0 and tupla[1] % 2 == 0 and tupla[2] % 2 != 0 and tupla[3] % 2 == 0:
        
        nova_tupla = tupla[0], tupla[1], tupla[3]
        
        return nova_tupla

    elif tupla[0] % 2 == 0 and tupla[1] % 2 != 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
        
        nova_tupla = tupla[0], tupla[2], tupla[3]
        
        return nova_tupla
        
    elif tupla[0] % 2 != 0 and tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
        
        nova_tupla = tupla[1], tupla[2], tupla[3]
        
        return nova_tupla
        
    elif tupla[0] % 2 == 0 and tupla[1] % 2 == 0 and tupla[2] % 2 != 0 and tupla[3] % 2 != 0:
        
        nova_tupla = tupla[0], tupla[1]
        
        return nova_tupla
        
    elif tupla[0] % 2 == 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 == 0:
        
        nova_tupla = tupla[0], tupla[3]
        
        return nova_tupla
        
    elif tupla[0] % 2 != 0 and tupla[1] % 2 != 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
        
        nova_tupla = tupla[2], tupla[3]
        
        return nova_tupla
        
    elif tupla[0] % 2 == 0 and tupla[1] % 2 != 0 and tupla[2] % 2 == 0 and tupla[3] % 2 != 0:
        
        nova_tupla = tupla[0], tupla[2]
        
        return nova_tupla
        
    elif tupla[0] % 2 != 0 and tupla[1] % 2 == 0 and tupla[2] % 2 != 0 and tupla[3] % 2 == 0:
        
        nova_tupla = tupla[1], tupla[3]
        
        return nova_tupla

    elif tupla[0] % 2 != 0 and tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 != 0:
        
        nova_tupla = tupla[1], tupla[2]
        
        return nova_tupla