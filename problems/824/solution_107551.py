def uppCons(frase):
    i=0
    while i < len(frase)-1:
        if frase[i] in "bcdfghjklmnpqrstvwxyz":
            frase[i]=str.upper(frase[i])
            i=i+1

            return frase