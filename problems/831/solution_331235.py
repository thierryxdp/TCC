def lingua_p(k):
    k1=k.lower()
    l=list(k1)
    f=''
    for n in range(len(l)):
        if l[n]=='a':
            l[n]='a'+'p'
        if l[n]=='e':
            l[n]='e'+'p'
        if l[n]=='i':
            l[n]='i'+'p'
        if l[n]=='o':
            l[n]='o'+'p'
        if l[n]=='u':
            l[n]='u'+'p'
        f=f+l[n]
    return f