def filtraMultlipos(X=list,N=int):
    T=0
    R=[]
    Y=X[T]%N+X[T]//N
    while T<len(X):
        if Y==X[T]:
            list.append(R,T)
    T=T+1
    return R