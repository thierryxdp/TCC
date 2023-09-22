def uppCons(s):
    i=1
    s=s.lower()
    while i<len(s):
        if s[i] not in 'aeiouãéíóê':
            s=s.replace(s[i],s[i].upper())
            i+=1
        else:
            i+=1
    return s