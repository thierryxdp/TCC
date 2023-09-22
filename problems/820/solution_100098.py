#
def posLetra(s,l,n):
    i=0
    lis=l
    c=str.count(s,lis)
    if c<n:
        return -1
    while i<len(s):
        p=str.find(s,lis)
        lis=l[p+1:]
        i=i+1
    return p