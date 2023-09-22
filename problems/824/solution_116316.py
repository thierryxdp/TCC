def uppCons(frase):
    i=0
    s=''
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvxwyz":
           s += frase[i].upper()
        else:
            s += frase[i]
        i=i+1
    return s