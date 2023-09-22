def posLetra(texto,letra,n):
    if str.index(texto,letra)>=n:
        i=0
        u=0
        while i!=n:
            if str.find(texto,letra,u)!=-1:
                i=i+1
            u=u+1
        return u