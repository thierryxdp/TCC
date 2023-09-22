def conta_frases(frase):
    h=frase.replace(' ','')
    d = str.replace(h,('...'),' ')
    r = str.replace(d, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    g=d.split(' ')
    return g