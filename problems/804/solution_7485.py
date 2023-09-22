def filtra_pares (tup):
    """Retorna uma tupla contendo apenas os elementos pares da tupla original
    tupla --> tupla"""
    
    nova_tup = list()
    
    if tup[1]%2 == 0:
        nova_tup.append(tup[1])
        
    elif tup[2]%2 == 0:
        nova_tup.append(tup[2])        
    
    elif tup[3]%2 == 0:
        nova_tup.append(tup[3])
        
    elif tup[4]%2 == 0:
        nova_tup.append(tup[4])
        
    return tuple(nova_tup)