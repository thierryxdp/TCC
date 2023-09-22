def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    for c in consoantes:
        frase = frase.replace(c,c.upper())
    return frase