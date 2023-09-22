def posLetra(s,l,n):
    """j"""
    a=[]
    i=0
    t=s.count(l)
    while ( i < len(s)):
            if l in s[i]:
                a=a+[i]
                i=i+1
            else:
                a=a
                i=i+1
    return a[n-1]