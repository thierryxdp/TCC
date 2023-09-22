def conta_frases(frase):
    frase1= frase.split('. ')
    frase2= frase.split('!')
    frase3= frase.split('?')
    frase4= frase.split('...')
    return len(frase1,frase2,frase3,frase4)