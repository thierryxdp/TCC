def conta_frases(frase):
    x = str.split(frase,'.')
    y = str.split(frase,'!')
    z = str.split(frase,'?') 
    return len(x) + len(y) + len(z)