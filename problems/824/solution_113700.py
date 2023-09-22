def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    for c in consoantes:
        frase = frase.replace(c,c.upper())
    return frase