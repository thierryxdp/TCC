def conta_frases(frases):
    
    """Funçao que conta o numero de frases que aparecem no texto.
    As frases podem ser terminadas com ponto final, exclamaçao, interrogaçao ou reticencias"""
    
    a = str.count(frases,"...")
    b = str.count(frases,"!")
    c = str.count(frases,"?")
    d = str.count(frases,".")
    n = a+b+c+d
    
    if a>0:
        
        return n-3*a
    else:
        
        return n