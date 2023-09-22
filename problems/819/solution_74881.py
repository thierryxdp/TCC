def filtraMultiplos(numeros, n):
    ''' Dando como entrada uma lista de numeros e um numero n, a funcao re-
    torna uma outra lista contendo os elementos divisiveis por n;
    
    list, int(ou float) -> list '''
    
    multiplos = []
    elemento = 0
    
    while elemento < len(numeros):
        
        if numeros[elemento] % n == 0:
            
            multiplos = multiplos + [numeros[elemento]]
            
        elemento = elemento + 1
        
    return multiplos