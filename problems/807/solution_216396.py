def conta_frases(frase):
    """teste"""
    
    a = frase.count("...") 
    b = frase.count("!")
    c = frase.count("?")
    d = frase.count(".")
    
    if a>0:
        d = d-3*a
    
    return (a)+(b)+(c)+(d)