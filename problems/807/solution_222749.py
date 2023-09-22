def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> list"""
    a = len(str.split(texto,'.',1)) 
    b = len(str.split(texto,'!'))
    c = len(str.split(texto,'?'))
    d = len(str.split(texto,'...'))
    
    if a < 2:
        a = 0
    if b < 2:
        b = 0
    if c < 2:
        c = 0
    if d < 2:
        d = 0
        return (a-1)+(b-1)+(c-1)+(d-1)