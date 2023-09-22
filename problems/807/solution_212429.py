def conta_frases(frase):
    frase=str.replace(frase,'!','.')
    frase=str.replace(frase,'?','.')
    frase=str.replace(frase,'...','.')
    return len(str.strip(frase,'.'))