def inverte(texto):
    '''Recebe um texte e retorna ele invertido e com espaço no lugar de pontuações;str -> str'''
    a = str.join(' ',str.split(texto,'...'))
    b = str.join(' ',str.split(a,'-'))
    c = str.join(' ',str.split(b,';'))
    d = str.join(' ',str.split(c,':'))
    e = str.join(' ',str.split(d,'!'))
    f = str.join(' ',str.split(e,'?'))
    g = str.join(' ',str.split(f,','))
    h = str.join(' ',str.split(g,'.'))
    k = (str.split(h))
    list.reverse(k)
    s = str.strip(str.lower(str.join(' ',k)))
    return s