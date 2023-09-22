def conta_frases(frase):
    frase1 = str.split(frase,'.')
    frase2 = str.split(frase,'?')
    frase3 = str.split(frase,'!')
    frase4 = str.split(frase,'...')
    return len(frase4)+len(frase1)