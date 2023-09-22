def conta_frases(texto):
    texto = str.replace(texto, '...', '.')
    texto = str.replace(texto, '!', '.')
    texto = str.replace(texto, '?', '.')
    s = str.split(texto, '.')
    
    return len(s)-1