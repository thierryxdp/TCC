def conta_frases(frase):
    a=frase.split('.') + frase.split('?') + frase.split('!') + frase.split('...')
    return len(a)