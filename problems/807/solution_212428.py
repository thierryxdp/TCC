def conta_frases(frase):
    frase=str.replace(frase,'!','.')
    frase=str.replace(frase,'?','.')
    frase=str.replace(frase,'...','.')
    frase=str.strip(frase,'.')
    return len(frase)