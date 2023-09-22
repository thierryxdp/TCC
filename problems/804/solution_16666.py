def filtra_pares(numeros: tuple[int]) -> tuple[int]:
    '...'
    # Iniciando um armazenador do tipo tupla
    pares = tuple()
    
    # Verificar, um a um, quais numeros são pares
    if numeros[0]%2 == 0:
        # Adiciono os pares no armazenador
        pares = pares + (numeros[0],) # += (numeros[0],)
        
    if numeros[1]%2 == 0:
        # Adiciono os pares no armazenador
        pares = pares + (numeros[1],) # += (numeros[1],)
        
    if numeros[2]%2 == 0:
        # Adiciono os pares no armazenador
        pares = pares + (numeros[2],) # += (numeros[2],)
        
    if numeros[3]%2 == 0:
        # Adiciono os pares no armazenador
        pares = pares + (numeros[3],) # += (numeros[3],)
    
    return pares