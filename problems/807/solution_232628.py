def conta_frases(texto):
    x = texto.split('.','!')
    y = texto.split('?','...')
    
    return len(x) + len(y)