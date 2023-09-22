def inverte(frase):
    a = str.split(frase)
    aa = list.lower(a)
    b = aa[::-1]
    c = b.replace('!', ' ')
    d = c.replace('?', ' ')
    e = d.replace('.', ' ')
    f = e.replace(',', ' ')
    g = f.replace(':', ' ')
    h = g.replace(';', ' ')
    i = h.replace('-', ' ')
    
    return i