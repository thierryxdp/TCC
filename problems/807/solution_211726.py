def conta_frases(frase):
    f1=str.split(frase,'.') + str.split(frase,'!') + str.split(frase,'?') + str.split(frase,'...')
    t=len(f1)
    return t