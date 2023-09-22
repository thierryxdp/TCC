def conta_frases(frase):
    """
"""
    n = frase
    if '.' or '!' or '?' or '...' in n:
        n = str.split(n,'.')
    if '!' in n:
        n = str.split(n,'!')
    if '?' in n:
        n = str.split(n,'?')
    if '...' in n:
        n = str.split(n,'...')
    return n