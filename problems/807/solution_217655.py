def conta_frases(frase):
    p3 = str.split(frase,'...',1) 
    e = str.split(frase,'!')
    i = str.split(frase,'?')
    p = str.split(frase,'.',1)
    
    
    return len(p3 +e+i+p)