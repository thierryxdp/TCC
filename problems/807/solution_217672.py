def conta_frases(frase):
    p = str.split(frase,'.')   
    e = str.split(frase,'!')
    i = str.split(frase,'?')
    x =  len(p+e+i)
    return x