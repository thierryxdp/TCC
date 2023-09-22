def conta_frase (s):
    e= str.count (s,'!')
    i = str.count (s, '?')
    r = str.count (s, '...')
    s2 =  str.replace (s, '...', 'XXX')
    pf = str.count(s2,'.')
    return e + i + r + pf