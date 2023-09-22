def conta_frases(frase):
    a=frase.split('.') or frase.split('?') or frase.split('!') or frase.split('...')
    return len(a)