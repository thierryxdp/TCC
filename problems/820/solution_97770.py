def posLetra(frase,letra,x):
    w=list(frase)
    k=-1
    m=1
    l=0
    if list.count(w,letra)>=x and x==1:
        return list.index(w[k+1:],letra)
    elif list.count(w,letra)>=x and x>1:
        while m<x:
            k=list.index(w[k+l+1:],letra)
            l=list.index(w[k+1:],letra)+k+l
            m=m+1
        return l+1
    else:
        return -1