def conta_frases(frase):
    x = str.split(frase,'.')
    y = str.split(x,'!')
    z = str.split(x,'?') 
    return len(z)