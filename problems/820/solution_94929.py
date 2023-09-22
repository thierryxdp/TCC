def posLetra(s,l,n):
    x=list(range(0,len(s)+1))
    c=0

    f=[]
    while c< len(s):
        if s[c]!=l:
            list.append(f,c)
            
        c=c+1
    return f