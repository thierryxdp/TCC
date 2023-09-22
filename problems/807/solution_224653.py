def conta_frase(frase):
    frase.replace(frase,'...','.')
    frase.replace(frase,'!','.')
    frase.replace(frase,'?','.')
    return len(frase.split('.'))