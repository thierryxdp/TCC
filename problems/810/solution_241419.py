def inverte(frase):
    """Recebe uma frase e retorna o contrario da composição das frases.
    str -> str"""
    
    txt = frase
    separado = txt.split
    
    return ' '.join(reversed(separado))