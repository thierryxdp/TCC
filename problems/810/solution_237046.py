def inverte(frase):
    a = str.split(frase,'.')
    b = str.split(a,',')
    c = str.split(b,';')
    d = str.split(c,':')
    e = str.split(d,'!')
    f = str.split(e,'?')
    g = str.split(f,'-')
    h = str.lower(g)
    i = h[::-1]
    j = str.join(' ',i)
    
    
    
    return j