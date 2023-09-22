def conta_frases(frase):
    frase=str.replace(frase,'?','.')
    frase=str.replace(frase,'...','.')
    frase=str.replace(frase,'!','.')
    frase=str.split(frase,'.')
    frase=str.join(' ',(frase))
    return frase