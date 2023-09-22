def conta_frases(frase):
    if '...' in frase:
        str.replace(frase,'...','.')
    if '!' in frase:
        str.replace(frase,'!','.')
    if '?' in frase:
        str.replace(frase,'?','.')
    return len(frase.split('.'))