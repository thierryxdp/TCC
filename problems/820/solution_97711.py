def posLetra(frase,letra,x):
    w=list(frase)
    k=0
    j=-1
    if list.count(w,letra)>=x:
        while k<x:
            j=j+1
            list.index(w[j:],letra)
            j=list.index(w[j:],letra)
            k=k+1
        return j
    else:
        return -1