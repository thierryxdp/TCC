def uppCons(f):
    novafrase=''
    i=0
    while i<len(f):
        if f[i] in 'bcdfghjklmnpqrstvwxyz':
            novafrase=novefrase+str(caractere.upper(f[1]))
        i=i+1
    return novafrase