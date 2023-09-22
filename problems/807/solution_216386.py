def conta_frases(frase):
    """teste"""
    
    a = frase.split("...") 
    b = frase.split("!")
    c = frase.split("?")
    d = frase.split(".")
    
    return len(a)+len(b)+len(c)+len(d)