def inverte(frase):
    x = str.replace(frase, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    g = a.split(' ')
    f = g[::-1]
    return ' '.join(f)