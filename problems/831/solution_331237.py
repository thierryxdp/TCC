def lingua_p(k):
    k1=k.lower()
    l=list(k1)
    f=''
    for n in range(len(l)):
        if l[n]=='á':
            l[n]='á'+'p'+'á'
        if l[n]=='a':
            l[n]='a'+'p'+''
        if l[n]=='e':
            l[n]='e'+'p'+'e'
        if l[n]=='é':
            l[n]='é'+'p'+'é'
        if l[n]=='i':
            l[n]='i'+'p'+'i'
        if l[n]=='o':
            l[n]='o'+'p'+'o'
        if l[n]=='u':
            l[n]='u'+'p'+'u'
        if l[n]=='ú':
            l[n]='ú'+'p'+'ú'
        f=f+l[n]
    return f