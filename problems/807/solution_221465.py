def conta_frases(texto):
    frase=texto.split('...')
    frase2=texto.split('!')
    frase3=texto.split('.')
    frase4=texto.split('?')
    if '...' in texto:
        return (len(frase)-4)+(len(frase2)-1)+(len(frase3)-1)+(len(frase4)-1)
    else:
        return (len(frase)-1)+(len(frase2)-1)+(len(frase3)-1)+(len(frase4)-1)