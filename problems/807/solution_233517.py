def conta_frases(frase):
    """
"""
    n = frase
    pontos= '.'
    exclamcao='!'
    
    if '.' in n:
        n = str.split(n,pontos)
    if '!' in n:
        n = str.split(n,'!')
    if '?' in n:
        n = str.split(n,'?')
    if'...' in n:
        n = str.split(n,'...')
    return n