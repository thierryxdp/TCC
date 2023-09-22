def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> list"""
    a = len(str.split(texto,'.'))
    b = len(str.split(texto,'!'))
    c = len(str.split(texto,'?'))
    d = len(str.split(texto,'...'))
    
    if a < 2:
        va = 0
    if b < 2:
        vb = 0
    if c < 2:
        vc = 0
    if d < 2:
        vd =0
        return va+vb+vc+vd