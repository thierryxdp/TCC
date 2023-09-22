def uppCons(s):
    i=
    s=s.upper()
    while i<len(s):
        if s[i] in 'AEIOãéí':
            s=s.replace(s[i],s[i].lower())
            i+=1
        else:
            i+=1
    return s