def uppCons(frase):
    v=0
    i=0
    while v<len(frase):
        if frase[i] in "bcdfgjklmnpqrstvwxz":
            frase[i]==frase[i].upper()
        i=i+1
        v=v+1
    return frase