def uppCons(s):
    i=0
    while i<len(s):
        if s[i] not in 'AEIOU':
            s=s.replace(s[i],s[i].upper())
            i+=1
        else:
            i+=1
    return s