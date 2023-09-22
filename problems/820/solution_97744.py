def posLetra(frase,letra,x):
    w=list(frase)
    k=-1
    if list.count(w,letra)>=x and x==1:
        return list.index(w[k+1:],letra)
    elif list.count(w,letra)>=x and x==2:
        k=list.index(w[k+1:],letra)
        return list.index(w[k+1:],letra)+1
    else:
        return -1