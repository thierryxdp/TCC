def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    frase2 = ''
    i = 0
    while i < len(frase):
        if frase[i] in consoantes:
            frase2 = frase2 + frase[i].upper()
        else:
            frase2 = frase2 + frase[i]
        i = i + 1
    return frase2