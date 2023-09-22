def uppCons(s):
    i=0
    while s[i]<len(s):
        if s[i]!='a' or s[i]!='e' or s[i]!='i' or s[i]!='o' or s[i]!='u':
            s.replace(s[i],s[i].upper())
            i+=1
        else:
            i+=1
    return s