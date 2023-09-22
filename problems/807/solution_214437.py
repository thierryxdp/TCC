def conta_frases(texto):
    '''Dado um texto, a função retorna o número de frases contidas no mesmo.
    sendo os separadores pontuações quaisquer: exclamação, reticências etc.;
    str -> int'''
    x = str.count(texto, '.')
    y = str.count(texto, '!')
    w = str.count(texto, '?')
    z = str.count(texto, '...')
    if '.' in texto:
        t = x
    if '!' in texto:
        u = y
    if '?' in texto:
        a = w
    if '...' in texto:
        n = z
    else:
        n = 0, t = 0, a = 0, u = 0
    return t+u+a+n