def conta_frases(texto):
    """Dado um texto, conta o número de frases nele presente.
       Cada frase termina com ".","!","?" ou "...".
       str -> int"""
    
    result = texto.replace('!','.')
    result = texto.replace('?','.')
    result = texto.replace('...','.')
    
    return result.count(.)