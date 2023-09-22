def posLetra(s,l,n):
    """Recebe uma string uma letra e um número e indica a ocorrëncia desejada da letra."""
    a=[]
    i=0
    t=s.count(l)
   
    while ( i < len(s)):
            if t<n:
                return -1
            if l in s[i]:
                a=a+[i]
                i=i+1
            else:
                a=a
                i=i+1
    return a[n-1]