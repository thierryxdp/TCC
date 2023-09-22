def posLetra(s,l,n):
    """s"""
    i=0
    a=int(s.count(l))
    x=""
            
    if a<n:
        return -1
    while (i<l):
        if l in str(s[i]):
            x= x+ str(i)
            i=i+1
        elif l not in str(s[i])
            i=i+1
            
    return x[n]