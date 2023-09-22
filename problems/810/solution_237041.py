def inverte(frase):
    a = frase.replace('!', ' ')
    b = a.replace('?', ' ')
    c = b.replace('.', ' ')
    d = c.replace(',', ' ')
    e = d.replace(':', ' ')
    f = e.replace(';', ' ')
    g = f.replace('-', ' ')
    h = g[::-1]
    i = str.lower(h)
    
    return i