def conta_frases(frase):
    frase.replace(frase,'...','.')
    frase.replace(frase,'!','.')
    frase.replace(frase,'?','.')
    return len(frase.split('.'))