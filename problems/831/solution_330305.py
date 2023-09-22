def lingua_p (palavra):
    """..."""
    g=palavra.lower()
    y=0
    x='p'
    vogal='aeiou'
    aux=''
    while y<len(palavra):
        if palavra[y] in vogal:
            aux=aux+palavra[y]+x+palavra[y] 
        if palavra[y] not in vogal:
            aux=aux+palavra[y]
        y+=1
    
    return aux