def conta_frases(frase):
    str.replace(frase,'...','.')
    str.replace(frase,'!','.')
    str.replace(frase,'?','.')
    str.split(frase,'.')
    return len(frase) -1