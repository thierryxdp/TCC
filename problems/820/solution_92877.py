def posLetra(s,l,n):
    i=0
    c=0
    while i<len(s):
        if s[i]==l:
            i+=1
            c+=1
        else:
            i+=1
    if n==c:
        return n
    else:
        return -1