def uppCons(f):
    novafrase=''
    i=0
    while i<len(f):
        if f[i] in 'bcdfghjklmnpqrstvwxyz':
            novafrase=novafrase+str(str.upper(f[1]))
        i=i+1
    return novafrase