def filtraMultiplos(ls,n):
    """
    define quais elementos da lista ls são multiplos de n
    list(int),int->list
    """
    X=[]
    for i in ls:
    	if i%n==0:
            X=X+[i]
    return X