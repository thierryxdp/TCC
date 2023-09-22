def inverte(f):
    a = str.join(' ', str.split(f, '.'))
    b = str.join('', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
    separei = e.split(' ')
    opo = separei[-1:-(len(separei)+1):-1]
    together = str.strip(str.join(' ',opo))
    
    return str.lower(together)