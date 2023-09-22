def conta_frases(texto):
    p = len(texto[:].split('.'))
    e = len(texto[:].split('!'))
    i = len(texto[:].split('?',0))    
    return p+e+i - 5