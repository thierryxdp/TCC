def conta_frases(frases):
    """Esta função retorna o número de frases contidas no texto.
       String --> int"""
    
    x = frase.split (".,!,?,... ")
    return len(x)