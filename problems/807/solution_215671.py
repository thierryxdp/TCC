def conta_frases(frase):
    frase1 = str.split(frase,'.')
    frase2 = str.split(frase1,'?')
    if frase1 == True:
        frase2 = str.split(frase1,'?')
    if frase2 == True:
        frase3 = str.split(frase2,'...')
    if frase3 == True:
        frase4 = str.split(frase3,'!')
    return len(frase4)