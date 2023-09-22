def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> list"""
    a = len(str.split(texto,'.'))
    b = len(str.split(texto,'!'))
    c = len(str.split(texto,'?'))
    d = len(str.split(texto,'...'))
    
    if a < 2:
        va = 0
        elif b < 2:
            vb = 0
            elif c < 2:
                vc = 0
                elif d < 2:
                    vd = 0
                    return va+vb+vc+vd