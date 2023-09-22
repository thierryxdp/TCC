def conta_frases (s):
    e= str.count (s, '!')
    i = str.count (s, '?')
    r = str.count (s, '...')
    s2 = str.replace (s, '...', 'xxx')
    pf = str.count(s2, '.')
    return e + i + r + pf