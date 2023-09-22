def uppCons(frase):
    i = 0
    consoantes = 'bcdfchjklmnpqrstvwxyz'
    while i<len(frase):
        if frase[i] in consoantes:
            frase = frase.replace(frase[i],frase[i].upper())
        i=i+1
    return frase