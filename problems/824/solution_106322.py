def uppCons(s):
    i=1
    s=s.upper()
    while i<len(s):
        if s[i] in 'AEIOUãéí':
            s=s.replace(s[i],s[i].lower())
            i+=1
        else:
            i+=1
    return s