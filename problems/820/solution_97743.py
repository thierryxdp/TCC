def posLetra(frase,letra,x):
    w=list(frase)
    k=-1
    j=1
    l=0
    if list.count(w,letra)>=x and x==1:
        return list.index(w[k+1:],letra)
    elif list.count(w,letra)>=x and x>1:
        while j<x:
            k=list.index(w[k+1:],letra)
            l=list.index(w[k+1:],letra)+1+l
            j=j+1
        return l
    else:
        return -1