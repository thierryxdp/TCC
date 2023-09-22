def filtraMultiplos(numeros, n):
    """recebe uma lista de numeros e um numero n e retorna uma lista com os
    numeros que forem multiplos de n
    list, int -> list"""
    
    i = 0
    multiplos = []
    
    while i < len(numeros):
        
        if isinstance(numeros[i] % n, int):
            list.append(multiplos, numeros[i])
            
        i += 1
    
    return multiplos