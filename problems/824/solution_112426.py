def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i]in'bcdfghjklmnpqrstvwxyzç':
            frase=frase[0:i]+frase[i].upper()+frase[i+1:]
        i=i+1
    return frase