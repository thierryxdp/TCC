def filtra_pares(numeros: tuple) -> tuple:
    """Filtra a tupla da entrada, retornando uma tupla apenas com os 
       elementos pares da entrada, na ordem em que se encontram 
       originalmente.
    """
    filtrados = tuple()
    
    if (numeros[0] % 2 == 0):
        filtrados += (numeros[0],)
    if (numeros[1] % 2 == 0):
        filtrados += (numeros[1],)
    if (numeros[2] % 2 == 0):
        filtrados += (numeros[2],)
    if (numeros[3] % 2 == 0):
        filtrados += (numeros[3],)
        
    return filtrados