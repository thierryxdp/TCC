def posLetra(texto,letra,n):
    if str.count(texto,letra)<n:
        return -1
    else:
        i=0
        l=0
        while i!=n:
            l=str.index(texto,letra,l)
            
            i=i+1
        return l