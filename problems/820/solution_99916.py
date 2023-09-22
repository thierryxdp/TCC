def posLetra(s,l,n):
    """s"""
    i=0
    a=int(s.count(l))
    x=""
            
    if a<n:
        return -1
    while (i<int(len(s))):
        if l in str(s[i]):
            x= x+ str(i)
            i=i+1
        else:
            i=i+1
            
    return x[n-1]