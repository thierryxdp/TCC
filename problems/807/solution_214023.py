def conta_frases(texto):
    """Dado um texto, retorna o número de frases nele presentes.
       str -> int"""
    
    return len(texto.split('.' and '!"))