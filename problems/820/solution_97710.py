def posLetra(frase,letra,x):
    w=list(frase)
    k=0
    j=0
    if list.count(w,letra)>=x:
        while k<x:
            list.index(w[j:],letra)
            j=list.index(w[j:],letra)+1
            k=k+1
        return j
    else:
        return -1