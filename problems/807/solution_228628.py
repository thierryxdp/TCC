def conta_frases(texto):
    a = str.join(' ', str.split(texto, '.'))
    c = str.join(' ', str.split(a, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '...'))
    numero=len(e.split())
    return numero