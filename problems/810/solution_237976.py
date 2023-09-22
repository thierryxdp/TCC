def inverte(x):
    a = str.replace(x, '.',' ')
    b = str.replace(a, ',',' ')
    c = str.replace(b, '!',' ')
    d = str.replace(c, ':',' ')
    e = str.replace(d, ';',' ')
    f = str.replace(e, '?',' ')
    g = str.replace(f, '-',' ')
    h = str.lower(g)
    i = str.split(h)
    j = i[::-1]
    k = str.join(' ',j)
    
    
    return k