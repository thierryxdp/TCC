def conta_frases(frases):
    frase1 = str.replace(frase,'?','.')
    frase2 = str.replace(frase,'!','.')
    frase3 = str.replace(frase,'...','.')
    frases = (frase1,frase2,frase3)
    frasefinal = str.split(frases,'.')
    return len(frasefinal)