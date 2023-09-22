def conta_frases(texto):
    """retorna por quantas frases o texto é formado"""
    """str -> int"""
    if '!' in texto:
        texto.replace('!','.')
    if '?' in texto:
        texto.replace('?','.')
    if '...' in texto:
        texto.replace('...','.')
    return len(texto.split('.'))