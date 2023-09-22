def conta_frases(texto):
    """Dado um texto, conta o número de frases nele presente.
       Cada frase termina com ".","!","?" ou "...".
       str -> int"""
    
    result = texto.replace('!','.')
    result = result.replace('?','.')
    result = result.replace('...','.')
    
    return result.count(.)