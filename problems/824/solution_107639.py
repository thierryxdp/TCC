def uppCons(frase):
    i=0
    while i < len(frase)-1:
        if frase[i] in "bcdfghjklmnpqrstvwxyz":
            frase[i]= frase[i].upper()
        i=i+1

    return frase