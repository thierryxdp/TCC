def conta_frases(texto):
    a = str.join('#', str.split(texto, '.'))
    c = str.join('#', str.split(a, '?'))
    d = str.join('#', str.split(c, '!'))
    numero=len(d.split("#"))
    return numero