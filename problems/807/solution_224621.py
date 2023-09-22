def conta_frases(texto):
    """retorna o numero de frases no texto; str -> int"""
    x=str.count(texto,'...')
    y=str.count(texto,'!')
    z=str.count(texto,'?')
    w=str.count(texto,'.')
    return abs(x-3*w)+y+z+w