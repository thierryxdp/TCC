def filtraMultiplos(lista,n):
    multiplos = [] 
    i = 0
    
    while i < len(lista):
        if lista[i] % n == 0:
            multiplos += lista[i]
        i += 1
    return multiplos