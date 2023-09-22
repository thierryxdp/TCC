def filtraMultiplos(X=list,N=int):
    T=0
    R=[]
    
    while T<len(X):
        if X[T]%N==0:
            list.append(R,X[T])
        T=T+1
    return R