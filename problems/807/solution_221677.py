def conta_frases(frase):
    x = str.count(frase,'.') + str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'...')
    return x