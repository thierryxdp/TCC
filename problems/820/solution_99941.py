def posLetra(s,l,n):
    """s"""
    i=0
    a=int(s.count(l))
    x=""
    y=n-1
            
    if a<n:
        return -1
    while (i<int(len(s))):
        if l == str(s[i]):
            x= x+ str(i)
            i=i+1
        else:
            i=i+1
            x=x
    
    return int( x[y])