def inverte(x):
    a =  str.replace (x,'-',' ')
    b =  str.replace (a,',',' ')
    c = str.replace (b ,':',' ')
    d = str.replace (c,';',' ')
    e = str.replace (d, '.',' ')
    f = str.replace (e, '!',' ')
    g = str.replace (f, '?',' ')
    h = g

    minusc = str.lower (h)
    
    split = str.split (minusc)
    return ' '.join (split[::-1])