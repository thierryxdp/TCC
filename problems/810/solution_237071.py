def inverte(frase):
    a = frase.replace('!', ' ')
    b = a.replace('?', ' ')
    c = b.replace('.', ' ')
    d = c.replace(',', ' ')
    e = d.replace(':', ' ')
    f = e.replace(';', ' ')
    g = f.replace('-', ' ')
    h = str.split(g,' ') 
    i = h[::-1]
    j = str.join(' ',i)
    
    
    return str.lower(j)