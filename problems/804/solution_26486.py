def filtra_pares():
    
    pares = []
    for item in tupla:
        if(item % 2 == 0):
            pares.append(item)
            
    return tuple(pares)