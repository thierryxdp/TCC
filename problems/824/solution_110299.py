def uppCons(frase):
    i=len(frase)
    while i-1<len(frase):
        if frase[i-1] in 'aeiou':
            frase= frase[i].lower()
        if frase[i-1] in 'bcdfghjklmnpqrstvwxyzç':
            frase= frase[i].upper()
        i=i-1
    return frase