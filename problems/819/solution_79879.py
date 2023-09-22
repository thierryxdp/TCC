def filtraMultlipos(X=list,N=int):
    T=0
    R=[]
    while T<len(X):
        if X[T]%N==int:
            list.append(R,T)
    T=T+1
    return R