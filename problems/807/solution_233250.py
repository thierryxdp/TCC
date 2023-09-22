def conta_frases(frases):
    
    """Dada varias frases, retorne o número de frases dos textos;; Str -> int """
    
    frases=frases.replace('!', '.')
    
    frases=frases.replace('?', '.')    
    
    frases=frases.replace('…', '.')
    
    return (len(frases.split('. ')))