def filtra_pares(a, b, c, d):
    """Filtra a tupla recebida voltando uma tupla apenas com os pares da tupla original, mas na mesma ordem;
    tupla -> tupla"""
    
    pares = []
    
    if a%2 == 0:
        pares.append(a)
    if b%2 == 0:
        pares.append(b)
    if c%2 == 0:
        pares.append(c)
    if d%2 == 0:
        pares.append(d)
        
    return pares