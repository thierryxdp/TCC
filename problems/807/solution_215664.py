def conta_frases(frase):
    frase1 = str.split(frase,'.')
    frase2 = str.split(frase1,'?')
    frase3 = str.split(frase2,'!')
    frase4 = str.split(frase3,'...')
    return len(frase4)