def conta_frases(frase):
    """
"""
    n = frase
    pontos= '.'
    excla='!'
    inter='?'
    red='...'
    
    if '.' in n:
        n = + str.split(n,pontos)
    if '!' in n:
        n = str.split(n,excla)
    if '?' in n:
        n = str.split(n,excla)
    if'...' in n:
        n = str.split(n, red)
    
    return len(n)