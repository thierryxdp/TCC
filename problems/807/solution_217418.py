def conta_frases(frases):
    """Função que conta o número de frases inseridas."""
    """Str -> Int"""
    
    return len(frases.split("...")) + len(frases.split("."))  + len(frases.split("!")) + len(frases.split("?"))