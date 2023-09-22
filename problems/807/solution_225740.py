def conta_frases(string):
    a = str.replace(string, '...' , '*')
    b = str.replace(a, '!' , '*')
    c = str.replace(b, '?' , '*')
    d = str.replace(c, '.' , '*')
    return str.count(d, '*')