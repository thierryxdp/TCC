def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> int"""
    a = str.count(texto, '.')
    b = str.count(texto, '!')
    c = str.count(texto, '?')
    d = str.count(texto, '...')
    if '.' and '...' and texto:
        c = -2
    else:
        a = a
        b = b
        c = c
        d = d
    
    return a+b+c+d