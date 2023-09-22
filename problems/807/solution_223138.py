def conta_frases(frases):
    frase1 = str.replace(frases,'?','.')
    frase2 = str.replace(frases,'!','.')
    frase3 = str.replace(frases,'...','.')
    frases = str.split(frases1,'.')
    return len(frases)