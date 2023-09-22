def conta_frases(frase):
    h=frase.replace(' ','')
    r = str.replace(h, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a