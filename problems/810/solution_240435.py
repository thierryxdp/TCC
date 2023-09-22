def inverte(frases):
    a = frases.replace('–', ' ')
    b = a.replace(',', ' ')
    c = b.replace(':', ' ')
    d = c.replace(';', ' ')
    e = d.replace('!', ' ')
    f = e.replace('?', ' ')
    g = f.replace('...', ' ')
    h = g.replace('.', ' ')
    i = h.replace('-', ' ')
    j = i.lower()
    k = str.split(j)
    l = k.reverse()
    return l