#
def posLetra(s,l,n):
    i=0
    lis=()
    c=str.count(s,l)
    if c<n:
        return -1
    while i<len(s):
        p=str.append(lis,str.find(s,l))        
        i=i+1
    return lis