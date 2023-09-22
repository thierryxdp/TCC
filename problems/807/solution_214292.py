def conta_frases(frase):
    x = frase.split('?') and frase.split('!')
    return len(x)