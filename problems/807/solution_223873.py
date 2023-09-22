def conta_frases(texto):
    """retorna por quantas frases o texto é formado"""
    """str -> int"""
    if '!' in texto:
        texto = str.replace(texto,'!','.')
    if '?' in texto:
        texto = str.replace(texto,'?','.')
    if '...' in texto:
        texto = str.replace(texto,'...','.')
    return len(str.split(texto,'.'))