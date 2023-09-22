def posLetra(s,l,o):
    i=0
    c=0
    while i<len(s):
        if s[i]==l:
            c=c+1
        if c==o:
            return i
        i+=1
    return -1