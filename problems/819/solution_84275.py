def filtraMultiplos(ls,n):
    """
    define quais elementos da lista ls são multiplos de n
    list(int),int->list
    """
    X=[]
    for i in ls:
        if n%i=0:
            X+=i
    return X