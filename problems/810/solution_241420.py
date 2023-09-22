def inverte(frase):
    """Recebe uma frase e retorna o contrario da composição das frases.
    str -> str"""
    
    separado = frase.split
    contrario = reversed(separado)
    
    return ' '.join(contrario)