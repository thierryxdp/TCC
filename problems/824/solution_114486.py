def uppCons(frase):
    i = 0
    consoantes = 'bcdfchjklmnpqrstvwxyz'
    while i<len(frase):
        if frase[i] in consoantes:
            frase[i].upper()
        i=i+1
    return frase