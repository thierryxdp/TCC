def uppCons(s):
    i=0
    while i<len(s):
        if s[i] in 'AEIOU':
            i+=1
        elif s[i] not in 'aeiouãéíóêú':
            s=s.replace(s[i],s[i].upper())
            i+=1
        else:
            i+=1
    return s