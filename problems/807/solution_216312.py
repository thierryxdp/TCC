def conta_frases(frase):
    frase1= frase.split('. ')
    frase2= frase.split('!')
    frase3= frase.split('?')
    frase4= frase.split('...')
    s = len(frase1) + len(frase2) + len(frase3) + len(frase4)
    return len(s)