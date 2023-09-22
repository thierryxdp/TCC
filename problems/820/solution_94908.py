def posLetra(s,l,n):
    c=0
    j=str.count(s,l)
    t=str.find(s,l)
    s=[]
    while c< len(s):
        if s[c]==l:
            list.appens(s,s[c])
        c=c+1
    return s