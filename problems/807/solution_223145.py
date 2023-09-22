def conta_frases(frases):
    frase1 = str.replace(frases,'?','.')
    frase2 = str.replace(frases,'!','.')
    frase3 = str.replace(frases,'...','.')
    frases = str(frase1,frase2,frase3)
    frasefinal = str.split(frases,'.')
    return len(frasefinal)