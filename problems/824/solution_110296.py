def uppCons(frase):
    i=1
    while i<len(frase):
        if frase[i] in 'aeiou':
            frase= frase[i].lower()
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            frase= frase[i].upper()
        i=i+1
    return frase