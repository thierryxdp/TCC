def inverte(frase):
    h =frase.split(' ')
    d = h([0:-1:-1])
    e =' '.join(d)
    x = str.replace(e, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a