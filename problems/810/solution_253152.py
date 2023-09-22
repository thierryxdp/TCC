def inverte(frase):
    
	a = frase.lower()
    b = a.replace('–', ' ')
    c = b.replace(',', ' ')
    d = c.replace(':', ' ')
    e = d.replace(';', ' ')
    f = e.replace('.', ' ')
    g = f.replace('!', ' ')
    h = g.replace('?', ' ')
    i = h.replace('...', ' ')
    j = i.replace('-', ' ')
    k = j.split()
    k.reverse()
    l = ' '.join(k)
    return l