def conta_frases(frase):
    frase2 = str.replace(frase,'...','.')
    return str.count(frase2,'.') + str.count(frase2,'?') + str.count(frase2,'!')