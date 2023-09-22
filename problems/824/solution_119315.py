def uppCons(frase):
    i=0
    r=[]
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyz":
        r=str.upper(frase[i])
        i=i+1
    return r