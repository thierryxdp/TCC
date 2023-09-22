def conta_frases(string):
    a = str.replace(string, '...' , '*')
    return str.replace(a, '!' , '*')