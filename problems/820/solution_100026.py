#
def posLetra(s,l,n):
    i=0
    p=0
    c=str.count(s,l)
    if c<n:
        return -1
    while i<len(s):
        p=p+str.find(s,l)        
        i=i+1
    return p