def conta_frases(frase):
    p = str.split(frase,'...')
    e = str.split(frase,'.')
    
    return len(p+e)