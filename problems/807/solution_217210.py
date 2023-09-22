def conta_frases(frase):
    x = str.split(frase,'.')
    y = str.split(frase,'!')
    z = str.split(frase,'?') 
    p = str.split(frase,'.''.''.'') 
    return len(x) - 1 + len(y) -1 + len(z) -1 + len(p) -1