def conta_frases(texto):
    """Esta função retorna o número de frases contidas no texto.
       String --> int"""
    
    x = texto.split (".")
    return len(x)