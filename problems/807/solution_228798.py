def conta_frases(string):
    a = str.count(string, '?')
    b = str.count(string, '!')
    c = str.count(string, '...')
    d = a+b+c
    e = str.replace(string, '...', 'oi')
    f = str.count(e, '.')
    return d+f