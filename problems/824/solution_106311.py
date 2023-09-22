def uppCons(s):
    i=0
    while i<len(s):
        if s[i] in not 'AEIOUaeiou':
            s.replace(s[i],s[i].upper())
            i+=1
        else:
            i+=1
    return s