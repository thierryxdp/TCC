def uppCons(frase):
    consoantes = 'bcdfghijklmnpqrstvxzwy'
    i = 0
    while i < len(frase):
        if frase[i] in consoantes:
            frase[i].upper()
            i = i + 1
    return frase