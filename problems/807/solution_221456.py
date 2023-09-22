def conta_frases(texto):
    frase=texto.split('.')
    frase2=texto.split('!')
    frase3=texto.split('...')
    frase4=texto.split('?')
    return len(frase)+len(frase2)+len(frase3)+len(frase4)