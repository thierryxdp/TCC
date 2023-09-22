def filtra_pares(tupla):
    """filtra os numeros pares de uma determinada tupla -> tupla"""
    tupla2 = tuple()
    if (tupla[0]%2)==0:
        tupla2 = tupla2 + (tupla[0],)
        
    if (tupla[1]%2)==0:
        tupla2 = tupla2 + (tupla[1],)
        
    if  tupla[2]%2)==0:
        tupla2 = tupla2 + (tupla[2],)
        
        return tupla