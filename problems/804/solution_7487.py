def filtra_pares (tup):
    """Retorna uma tupla contendo apenas os elementos pares da tupla original
    tupla --> tupla"""
    
    nova_tup = list()
    
    if tup[0]%2 == 0:
        nova_tup.append(tup[0])
        
    if tup[1]%2 == 0:
        nova_tup.append(tup[1])        
    
    if tup[2]%2 == 0:
        nova_tup.append(tup[2])
        
    if tup[3]%2 == 0:
        nova_tup.append(tup[3])
        
    return tuple(nova_tup)