def conta_frases(texto):
    
    x = texto.replace('?', '.')
    y = x.replace('!', '.')
    z = y.replace('...', '.')
    w = z.split('.')
    w.remove('')
    return len(w)