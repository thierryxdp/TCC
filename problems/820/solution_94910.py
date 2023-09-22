def posLetra(s,l,n):
    c=0
    j=str.count(s,l)
    t=str.find(s,l)
    u=[]
    while c< len(s):
        if s[c]==l:
            list.append(u,s[c])
        c=c+1
    return u