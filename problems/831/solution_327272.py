def lingua_p(palavra):
    '''A função recebe como parametro uma palavra e retorna esta mesma palavra para a lingua do p.
    str -> str'''
    x = str.replace(palavra,'a', 'apa')    
    y = str.replace(x,'e', 'epe')
    z = str.replace(y,'i', 'ipi')
    w = str.replace(z,'o', 'opo')
    k = str.replace(w,'u', 'upu')
    s = str.replace(k,'á', 'ápá')    
    d = str.replace(s,'é', 'épé')
    f = str.replace(d,'í', 'ípí')
    g = str.replace(f,'ó', 'ópó')
    h = str.replace(g,'ú', 'úpú')
    
    return h