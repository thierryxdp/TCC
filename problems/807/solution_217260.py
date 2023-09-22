def conta_frase(frase):
    frase = frase.replace('!','.')
    frase = frase.replace('...','.')
    frase = frase.replace('?','.')
    frase = frase.split('.')

    return len(frase) - 1