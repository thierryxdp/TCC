import re
def conta_frases(texto):
    """Retorna o número de frases de uma string;
    str -> int"""
    if '!' in texto:
        return len(texto.split('!'))
    elif '?' in texto:
        return len(texto.split('?'))
    elif '... ' in texto:
        return len(texto.split('... '))
    elif '. ' in texto:
        return len(texto.split('. '))
    elif '...' in texto:
        return len(texto.split('...'))
    if '!' or '?' or '...' or '... ' or '.' or '. ' in texto:
        return len(re.split('! ? .  ... .'))