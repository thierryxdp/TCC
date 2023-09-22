def conta_frases(frase):
    p = str.split(frase,'.')   
    e = str.split(frase,'!')
    i = str.split(frase,'?')
    p3 = str.split(frase,'...')
    x =  len(p)+len(e)+len(i)+len(p3) 
    return x