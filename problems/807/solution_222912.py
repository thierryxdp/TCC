def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> list"""
    a = len(str.split(texto,'.',1)) 
    b = len(str.split(texto,'!',1))
    c = len(str.split(texto,'?',1))
    d = len(str.split(texto,'...',1))
    
    if a and (a or b) and (a or c) and (a or d) and (b or c) and (b or d) and (c or d)  < 2:
        a = 0
        b = 0
        c = 0
        d = 0
        return (a + b + c + d)
    else:
        a = a
        b = b
        c= c
        d = d
        return round ((a+b+c+d)/2)