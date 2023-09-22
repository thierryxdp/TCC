def posLetra(st,l,n):
    p=0
    for i in range(len(st)):
        if st[i]==l:
            p+=1
        if p==l:
            return i
    return -1