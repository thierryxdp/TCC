def posLetra(frase,L,N):
    c=0
    f=[]
    while c<len(frase):
        if frase[c]==L:
            f=f+[c]
            if(len(f)+1)<=N:
                x=-1
            if(len(f)+1)>N:
                x=f[N-1]
        c=c+1
    return x