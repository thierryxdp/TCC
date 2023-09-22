def conta_frases(frase):
    p = str.split(frase,'...')
    e = str.split(frase,'!')
    i = str.split(frase,'?')
    
    
    return len(p +e+i)