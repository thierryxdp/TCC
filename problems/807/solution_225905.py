def conta_frases(texto):
    """conta o numero de frases de um texto"""
    x=len(str.strip(texto,'.'))
    w=len(str.strip(texto,'?'))
    y=len(str.strip(texto,'!'))
    z=len(str.strip(texto, '...'))
    n= x+w+y+z
    return n