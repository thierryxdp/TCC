def conta_frases(frase):
    p = str.split(frase,'.')   
    e = str.split(frase,'!')
    i = str.split(frase,'?')
    p3 = str.split(frase,'...')
    x =  len(p)-1
    y = len(e)-1
    return x+y