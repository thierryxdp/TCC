def uppCons(frase):
    i=0
    acumula=""
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstxvwyzç":
            acumula=acumula+str.upper(frase[i])
        else: acumula=acumula+frase[i]
        i=i+1
    return acumula