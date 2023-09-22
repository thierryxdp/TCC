def uppCons(frase):
    c=0
    f=""
    while c<len(frase):
        if frase[c]in "bcdfghjklmnpqrstvwxzç":
            f+=str.upper(frase[c])
        else:
            s+=frase[c]
        c=c+1
    return f