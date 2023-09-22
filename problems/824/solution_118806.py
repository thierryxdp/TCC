def uppCons(frase):
    i=0
    frase1=frase[:]
    while i<len(frase):
        if frase1[i] in "bcdfghjklmnpqrstxvwyzç":
            frase1=str.upper(frase[i])
        i=i+1
    return frase1