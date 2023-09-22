def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> list"""
    a = len(str.split(texto,'.',1)) 
    b = len(str.split(texto,'!',1))
    c = len(str.split(texto,'?',1))
    d = len(str.split(texto,'...',1))
    
    if a < 2:
        a = 0
    if b < 2:
        b = 0
    else:
        b = 1
    if c < 2:
        c = 0
    else:
        c = 1
    if d < 2:
        d = 0
    else:
        d = 1
        
        return a+b+c+d