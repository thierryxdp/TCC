def posLetra(frase,letra,n):
    i=0
    v=[]
    if str.count(frase,letra)>n:
        return -1
    while i<len(frase):
        if frase[i]=letra:
            v=v+[i,]
            i=i+1
        else:
            i=i+1
    return v[n-1]