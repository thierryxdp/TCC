def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstxvwyzç":
            frase=str.upper(frase[i])
            i=i+1
    return frase