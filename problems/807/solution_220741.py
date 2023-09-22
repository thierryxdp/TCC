def conta_frases(frase):
    x = str.replace(frase, ('-'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    h = a.split(' ')
    return len(h)