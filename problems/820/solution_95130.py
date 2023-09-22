def posLetra(frase,letra,n):
    i=0
    ap=[]
    while i<len(frase) and len(ap)!=n:
        if frase[i]==letra:
            list.append(ap,frase[i])
        else:
            i=-1
        i+=1
    return i,ap