def lingua_p(k):
    k1=k.lower()
    l=list(k1)
    f=''
    for n in range(len(l)):
        if l[n]=='a':
            l[n]='a'+'p'+'a'
        if l[n]=='e':
            l[n]='e'+'p'+'e'
        if l[n]=='i':
            l[n]='i'+'p'+'i'
        if l[n]=='o':
            l[n]='o'+'p'+'o'
        if l[n]=='u':
            l[n]='u'+'p'+'u'
        f=f+l[n]
    return f