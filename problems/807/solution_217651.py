def conta_frases(frase):
    p = str.split(frase,'...',1)
    e = str.split(frase,'!')
    i = str.split(frase,'?')
    
    
    return len(p +e+i)