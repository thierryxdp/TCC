def filtraMultiplos(X=list,N=int):
    T=0
    R=[]
    Y=X[T]//N
    while T<len(X):
        if Y==0:
            list.append(R,T)
    T=T+1
    return R